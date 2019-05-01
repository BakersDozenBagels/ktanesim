use crate::prelude::*;
use strum_macros::Display;

pub struct EventResponse {
    pub render: Option<Render>,
    pub message: Option<(String, String)>,
}

impl EventResponse {
    /// Turn the EventResponse into a message and send it.
    pub fn resolve(self, ctx: &Context, msg: &Message, bomb: &Bomb, module: &dyn Module) {
        match self {
            EventResponse {
                render: Some(render),
                message,
            } => {
                render.resolve(ctx, msg.channel_id, |m, file| {
                    m.embed(|e| {
                        e.image(file);
                        e.title(format!("{} (#{})", module.name(), module.number() + 1));
                        let manual = crate::modules::manual_url(module, bomb.data.rule_seed);
                        e.field("Manual", format!("[Click here]({})", manual), true);
                        e.field("Time remaining", bomb.data.timer.to_string(), true);

                        if module.descriptor().rule_seed
                            && bomb.data.rule_seed != ktane_utils::random::VANILLA_SEED
                        {
                            e.field("Rule seed", bomb.data.rule_seed, true);
                        }

                        if !module.state().solved() {
                            e.description(module.help_message());
                        }

                        if let Some(user_id) = module.state().user {
                            if let Some(user) = user_id.to_user_cached(&ctx.cache) {
                                let user = user.read();
                                e.footer(|ft| {
                                    if module.state().solved() {
                                        ft.text(format!("Solved by {}", user.name));
                                    } else {
                                        ft.text(format!("Claimed by {}", user.name));
                                    }

                                    ft.icon_url(&crate::utils::user_avatar(&user))
                                });
                            }
                        }

                        if let Some((title, description)) = message {
                            e.field(title, description, false);
                        }

                        e
                    })
                });
            }
            EventResponse {
                render: None,
                message: Some((title, description)),
            } => unimplemented!(),
            // some events don't need any response.
            EventResponse {
                render: None,
                message: None,
            } => {}
        }
    }
}

pub struct Render(pub Box<dyn FnOnce() -> (Vec<u8>, RenderType)>);

#[derive(Copy, Clone, PartialEq, Eq, Debug, Display)]
#[strum(serialize_all = "snake_case")]
pub enum RenderType {
    PNG,
    GIF,
}

use serenity::builder::CreateMessage;
impl Render {
    /// Helper method for simpler creation of Render objects
    pub fn with(f: impl FnOnce() -> (Vec<u8>, RenderType) + 'static) -> Render {
        Render(Box::new(f))
    }

    pub fn resolve<F>(self, ctx: &Context, channel_id: ChannelId, f: F)
    where
        for<'b> F: FnOnce(&'b mut CreateMessage<'b>, &str) -> &'b mut CreateMessage<'b>,
    {
        let (data, extension) = (self.0)();
        let filename = format!("f.{}", extension);
        if let Err(why) = channel_id.send_files(
            &ctx.http,
            std::iter::once((&data[..], &filename[..])),
            |m| f(m, &format!("attachment://{}", filename)),
        ) {
            error!("Couldn't send message with attachment: {:?}", why);
        }
    }
}
