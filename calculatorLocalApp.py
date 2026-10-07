import tkinter as tk

# Calculator state: current screen value, previous number, selected operator, and whether new input starts a fresh value.
current = "0"
previous = None
op = None
fresh = False

# Refresh the display so the screen shows the current value.
def update():
    display.config(text=current)

# Handle digit input and decimal entry.
def press(d):
    global current, fresh
    if current == "Error":
        current = "0"
    if fresh:
        current = "0." if d == "." else d
        fresh = False
    elif d == ".":
        if "." not in current:
            current += "."
    else:
        current = d if current == "0" else current + d
    update()

# Save the current value and choose the operator for the next calculation.
def choose_op(next_op):
    global previous, op, fresh
    if current == "Error":
        return
    if op is not None and not fresh:
        equals()
        if current == "Error":
            return
    previous = float(current)
    op = next_op
    fresh = True

# Perform the calculation based on the stored operator and result.
def equals():
    global current, op, fresh
    if op is None:
        return
    b = float(current)
    if op == "+":
        result = previous + b
    elif op == "-":
        result = previous - b
    elif op == "*":
        result = previous * b
    elif op == "/":
        result = "Error" if b == 0 else previous / b

    if result == "Error":
        current = "Error"
    else:
        current = str(round(result, 10)).rstrip("0").rstrip(".") if "." in str(round(result, 10)) else str(round(result, 10))
    op = None
    fresh = True
    update()

# Reset the calculator to zero and clear the stored calculation state.
def clear_all():
    global current, previous, op, fresh
    current, previous, op, fresh = "0", None, None, False
    update()

# Remove the last digit from the current number.
def backspace():
    global current
    if fresh or current == "Error":
        return
    current = current[:-1] if len(current) > 1 else "0"
    update()

# Create the window and set overall appearance.
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#333")
window.resizable(False, False)

# Create the display label where the current value is shown.
display = tk.Label(window, text="0", font=("Arial", 24), bg="#111827", fg="white",
                   anchor="e", padx=10, pady=12, width=12)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Build a reusable calculator button to keep the layout consistent.
def make_button(text, row, col, command, color="#e5e7eb", fg="black", colspan=1, rowspan=1):
    tk.Button(window, text=text, font=("Arial", 14), bg=color, fg=fg,
              command=command, width=4, height=1, bd=0, relief="groove",
              padx=4, pady=4, activebackground="#d1d5db",
              highlightthickness=0, borderwidth=1, cursor="hand2").grid(
        row=row, column=col, columnspan=colspan, rowspan=rowspan,
        padx=5, pady=5, sticky="nsew")

# Define the calculator buttons and assign their colors and actions.
make_button("C", 1, 0, clear_all, "#a80000", "white")
make_button("⌫", 1, 1, backspace, "#d1d5db")
make_button("÷", 1, 2, lambda: choose_op("/"), "#fbbf24", "black")
make_button("×", 1, 3, lambda: choose_op("*"), "#fbbf24", "black")

make_button("7", 2, 0, lambda: press("7"), "#f3f4f6")
make_button("8", 2, 1, lambda: press("8"), "#f3f4f6")
make_button("9", 2, 2, lambda: press("9"), "#f3f4f6")
make_button("−", 2, 3, lambda: choose_op("-"), "#fbbf24", "black")

make_button("4", 3, 0, lambda: press("4"), "#f3f4f6")
make_button("5", 3, 1, lambda: press("5"), "#f3f4f6")
make_button("6", 3, 2, lambda: press("6"), "#f3f4f6")
make_button("+", 3, 3, lambda: choose_op("+"), "#fbbf24", "black")

make_button("1", 4, 0, lambda: press("1"), "#f3f4f6")
make_button("2", 4, 1, lambda: press("2"), "#f3f4f6")
make_button("3", 4, 2, lambda: press("3"), "#f3f4f6")
make_button("=", 4, 3, equals, "#fbbf24", "black", rowspan=2)

make_button("0", 5, 0, lambda: press("0"), "#f3f4f6", "black", colspan=2)
make_button(".", 5, 2, lambda: press("."), "#f3f4f6")

# Start the Tkinter loop so the calculator window remains open and interactive.
window.mainloop()