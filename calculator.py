"""
=========================================================
            SIX DIGIT CALCULATOR
---------------------------------------------------------
Author : ChatGPT
Language : Python
Library : tkinter (built-in)

Features
---------
✓ Single File
✓ Premium UI
✓ Animated Buttons
✓ Hover Effects
✓ Smooth Press Animation
✓ 6 Digit Display
✓ Keyboard Friendly
=========================================================
"""

import tkinter as tk

# =========================================================
# COLORS
# =========================================================

BG = "#F2F3F5"
FRAME = "#FFFFFF"
DISPLAY_BG = "#ECEEF1"

BTN = "#FFFFFF"
BTN_HOVER = "#F4F5F7"
BTN_PRESS = "#D9DEE6"

TEXT = "#222222"
SECONDARY = "#666666"

ACCENT = "#3F6AE8"

# =========================================================
# WINDOW
# =========================================================

root = tk.Tk()
root.title("Calculator")
root.geometry("380x560")
root.configure(bg=BG)
root.resizable(False, False)

# =========================================================
# VARIABLES
# =========================================================

expression = ""
display_var = tk.StringVar(value="0")

# =========================================================
# FUNCTIONS
# =========================================================

def update_display():

    global expression

    if expression == "":
        display_var.set("0")
        return

    try:
        text = expression

        if len(text) > 12:
            text = text[-12:]

        display_var.set(text)

    except:
        display_var.set("Error")


def press(value):

    global expression

    expression += value
    update_display()


def clear():

    global expression

    expression = ""
    update_display()


def equal():

    global expression

    try:
        result = str(eval(expression))

        if "." in result:
            result = str(round(float(result), 4))

        if len(result) > 12:
            result = result[:12]

        expression = result
        update_display()

    except:
        display_var.set("Error")
        expression = ""


# =========================================================
# BUTTON ANIMATION
# =========================================================

def hover_in(widget):
    widget.config(bg=BTN_HOVER)


def hover_out(widget):
    widget.config(bg=BTN)


def click(widget):

    widget.config(bg=BTN_PRESS)

    root.after(
        90,
        lambda: widget.config(bg=BTN_HOVER)
    )


# =========================================================
# CUSTOM BUTTON
# =========================================================

def create_button(text, row, col, command):

    btn = tk.Label(
        buttons_frame,
        text=text,
        bg=BTN,
        fg=TEXT,
        font=("Segoe UI", 18),
        width=4,
        height=2,
        relief="flat",
        cursor="hand2"
    )

    btn.grid(
        row=row,
        column=col,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    btn.bind(
        "<Enter>",
        lambda e: hover_in(btn)
    )

    btn.bind(
        "<Leave>",
        lambda e: hover_out(btn)
    )

    btn.bind(
        "<Button-1>",
        lambda e: (
            click(btn),
            command()
        )
    )


# =========================================================
# DISPLAY
# =========================================================

display_frame = tk.Frame(
    root,
    bg=FRAME,
    padx=20,
    pady=25
)

display_frame.pack(
    fill="x",
    padx=18,
    pady=18
)

display = tk.Label(

    display_frame,

    textvariable=display_var,

    anchor="e",

    bg=DISPLAY_BG,

    fg=TEXT,

    padx=18,

    pady=25,

    font=("Consolas", 34)

)

display.pack(fill="both")

# =========================================================
# BUTTON AREA
# =========================================================

buttons_frame = tk.Frame(
    root,
    bg=BG
)

buttons_frame.pack(
    pady=5
)

for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)

# =========================================================
# BUTTONS
# =========================================================

buttons = [

    ("7", lambda: press("7")),
    ("8", lambda: press("8")),
    ("9", lambda: press("9")),
    ("/", lambda: press("/")),

    ("4", lambda: press("4")),
    ("5", lambda: press("5")),
    ("6", lambda: press("6")),
    ("*", lambda: press("*")),

    ("1", lambda: press("1")),
    ("2", lambda: press("2")),
    ("3", lambda: press("3")),
    ("-", lambda: press("-")),

    ("C", clear),
    ("0", lambda: press("0")),
    ("=", equal),
    ("+", lambda: press("+"))

]

index = 0

for r in range(4):

    for c in range(4):

        txt, cmd = buttons[index]

        create_button(
            txt,
            r,
            c,
            cmd
        )

        index += 1

# =========================================================
# KEYBOARD SUPPORT
# =========================================================

def key(event):

    ch = event.char

    if ch in "0123456789+-*/":
        press(ch)

    elif event.keysym == "Return":
        equal()

    elif event.keysym == "BackSpace":

        global expression

        expression = expression[:-1]
        update_display()

    elif event.keysym == "Escape":
        clear()


root.bind("<Key>", key)

# =========================================================
# START
# =========================================================

root.mainloop()