import os
import random
import modules

class EmojiMath(modules.Module):
    identifiers = ['emojimath']
    display_name = "Emoji Math"
    manual_name = "Emoji Math"
    help_text = "`{cmd} submit 23` or `{cmd} submit -71`. This will always press the `=` button."
    module_score = 3
    
    EMOJI = [
        ":)", "=(", "(:", ")=", ":(",
        "):", "=)", "(=", ":|", "|:"
    ]

    def __init__(self, bomb, ident):
        super().__init__(bomb, ident)
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        op = random.random() > 0.5 # Represents addition if true
        
        self.answer = num1
        if op:
            self.answer += num2
        else:
            self.answer -= num2
        
        self.display = ""
        if num1 > 9:
            self.display += EmojiMath.EMOJI[num1 // 10]
        self.display += EmojiMath.EMOJI[num1 % 10]
        self.display += "+" if op else "-"
        if num2 > 9:
            self.display += EmojiMath.EMOJI[num2 // 10]
        self.display += EmojiMath.EMOJI[num2 % 10]

        self.log(f"Display: {self.display}")
        self.log(f"Deciphered question: {num1} {"+" if op else "-"} {num2}")
        self.log(f"Solution: {self.answer}")

    def get_svg(self, led):
        return (f'<svg viewBox="-366 367 348 348" fill="#fff" stroke-linejoin="round" stroke-miterlimit="10" xmlns:xlink="http://www.w3.org/1999/xlink">'
            f'<path stroke="#000" stroke-width="2" d="M-360.9 372.8H-24v337.7h-336.9V372.8z"/>'
            f'<circle cx="298" cy="40.5" r="15" fill="{led}" stroke="#000" stroke-width="2"/>'
            f'<path fill="#000" d="M-341 391h232v72h-232z"/>'
            f'<path fill="#FFF" stroke="#000" stroke-width="1.3" d="M-323 489h53v53h-53zm0 64.5h53v53h-53zm0 65h53v53h-53zm66.1-129.5h53v53h-53zm0 64.5h53v53h-53zm0 65h53v53h-53zm67-129.5h53v53h-53zm0 64.5h53v53h-53zm0 65h53v53h-53zm67.6-129.5h53v53h-53zm0 64.5h53v53h-53zm0 65h53v53h-53z"/>'
            f'<path fill="#000" d="M-291.2 529.9h-3.5v-22.4q-1.3 1.2-3.4 2.4-2 1.2-3.7 1.8v-3.4q3-1.4 5.2-3.3 2.2-2 3.1-3.9h2.3zm70.3-3.4v3.4h-19q0-1.3.5-2.5.7-1.9 2.3-3.8 1.6-1.9 4.6-4.3 4.6-3.8 6.3-6 1.6-2.3 1.6-4.3t-1.5-3.5q-1.5-1.5-3.9-1.5-2.5 0-4 1.6-1.5 1.5-1.6 4.2l-3.6-.4q.4-4 2.8-6.1 2.4-2.2 6.5-2.2t6.5 2.3q2.4 2.3 2.4 5.7 0 1.7-.7 3.4-.7 1.6-2.3 3.4-1.6 1.9-5.4 5-3.2 2.7-4 3.7-1 1-1.6 1.9zm48.1-4.4 3.5-.5q.6 3 2 4.3 1.6 1.3 3.6 1.3 2.5 0 4.2-1.7 1.7-1.7 1.7-4.3 0-2.4-1.5-4-1.6-1.5-4-1.5-1 0-2.5.4l.3-3.1h.6q2.3 0 4-1.2 1.9-1.1 1.9-3.6 0-1.9-1.4-3.2-1.3-1.2-3.3-1.2-2 0-3.5 1.3-1.3 1.2-1.7 3.8l-3.5-.6q.6-3.5 3-5.5 2.2-2 5.6-2 2.3 0 4.3 1t3 2.8q1 1.8 1 3.7 0 1.9-1 3.4t-2.9 2.4q2.6.6 4 2.5 1.4 1.8 1.4 4.6 0 3.7-2.8 6.3-2.7 2.6-6.9 2.6-3.7 0-6.2-2.2-2.5-2.3-2.9-5.8zm67.7-6.6q0-5 1-8.2 1-3 3.1-4.7 2-1.7 5.2-1.7 2.3 0 4 1 1.8.8 3 2.6 1 1.7 1.7 4.3.6 2.5.6 6.7 0 5-1 8.2-1 3-3.1 4.7-2 1.7-5.2 1.7-4.1 0-6.5-3-2.8-3.5-2.8-11.6zm3.6 0q0 7 1.6 9.4 1.7 2.3 4.1 2.3 2.4 0 4-2.3 1.7-2.4 1.7-9.4t-1.6-9.4q-1.7-2.3-4.1-2.3-2.5 0-4 2-1.7 2.7-1.7 9.7zM-294 593.7V587h-12.4v-3.3l13-18.5h3v18.5h3.8v3.3h-3.9v6.8zm0-10v-13l-9 13zm54.1 2.7 3.7-.3q.4 2.7 1.9 4 1.5 1.4 3.6 1.4 2.5 0 4.3-2 1.8-1.9 1.8-5 0-3-1.7-4.8-1.7-1.7-4.5-1.7-1.7 0-3 .8-1.4.7-2.2 2l-3.3-.5 2.8-14.7h14.2v3.4h-11.4l-1.5 7.7q2.6-1.8 5.4-1.8 3.7 0 6.3 2.6 2.6 2.6 2.6 6.7 0 3.9-2.3 6.7-2.7 3.5-7.5 3.5-3.9 0-6.4-2.2-2.4-2.2-2.8-5.8zm85.4-13.9-3.5.3q-.4-2-1.3-3-1.4-1.5-3.5-1.5-1.7 0-3 1-1.6 1.1-2.6 3.4-1 2.4-1 6.7 1.3-2 3.1-2.9 1.9-1 3.9-1 3.5 0 6 2.7 2.5 2.5 2.5 6.6 0 2.7-1.2 5-1.2 2.4-3.2 3.6-2 1.2-4.6 1.2-4.4 0-7.2-3.2t-2.8-10.7q0-8.3 3.1-12 2.7-3.3 7.2-3.3 3.4 0 5.5 1.9 2.2 1.9 2.6 5.2zm-14.3 12.4q0 1.8.8 3.4.7 1.7 2.1 2.6 1.4.8 3 .8 2.2 0 3.8-1.8 1.6-1.8 1.6-4.9 0-3-1.6-4.6-1.6-1.7-4-1.7t-4 1.7q-1.7 1.7-1.7 4.5zm-137 49.3V631h18.6v2.7q-2.8 3-5.5 7.7-2.6 4.9-4.1 10-1 3.6-1.3 7.8h-3.7q.1-3.3 1.4-8.1 1.2-4.8 3.6-9.3 2.4-4.4 5-7.5zm71.4 9.4q-2.2-.8-3.2-2.3-1-1.5-1-3.5 0-3.2 2.2-5.3 2.2-2.1 6-2.1 3.7 0 6 2.2 2.3 2.1 2.3 5.3 0 2-1 3.4-1.1 1.5-3.3 2.3 2.7.9 4 2.8 1.4 1.9 1.4 4.5 0 3.7-2.6 6.2t-6.8 2.5q-4.2 0-6.8-2.5-2.6-2.5-2.6-6.3 0-2.7 1.4-4.6 1.4-2 4-2.6zm-.7-6q0 2 1.3 3.4 1.3 1.3 3.4 1.3 2 0 3.3-1.3 1.3-1.3 1.3-3.2 0-1.9-1.3-3.2-1.3-1.3-3.3-1.3-2 0-3.4 1.3-1.3 1.3-1.3 3zm-1.1 13.3q0 1.5.7 2.9t2.1 2.2q1.4.7 3 .7 2.6 0 4.2-1.6t1.6-4.1q0-2.6-1.7-4.2-1.6-1.7-4.2-1.7-2.5 0-4.1 1.7-1.6 1.6-1.6 4zm64 1.6 3.3-.3q.4 2.4 1.6 3.5 1.2 1 3.1 1 1.7 0 2.9-.7 1.2-.8 2-2t1.3-3.3q.5-2.2.5-4.3v-.7q-1 1.6-2.9 2.7-1.8 1-4 1-3.5 0-6-2.6-2.4-2.5-2.4-6.8t2.5-7q2.6-2.6 6.5-2.6 2.8 0 5 1.5 2.4 1.5 3.6 4.3 1.2 2.8 1.2 8 0 5.5-1.2 8.8-1.2 3.2-3.5 5-2.4 1.6-5.5 1.6-3.4 0-5.5-1.8-2.2-2-2.6-5.3zM-158 640q0-3-1.6-4.8-1.6-1.8-3.9-1.8t-4 2q-1.8 1.8-1.8 4.9 0 2.7 1.6 4.4 1.7 1.7 4.1 1.7 2.5 0 4-1.7 1.6-1.7 1.6-4.7zm71.6 2.4h-19V639h19zm0 8.7h-19v-3.3h19zm-14.9-69.2v-3.6h10.8v3.6z"/>'
            f'<text x="-225" y="427" text-anchor="middle" style="font-size:64pt;font-family:sans-serif;">{self.display}</text>'
            f'</svg>')

    @modules.check_solve_cmd
    async def cmd_press(self, author, parts):
        if not parts:
            return await self.usage(author)

    

    COMMANDS = {
        "submit": cmd_press
    }