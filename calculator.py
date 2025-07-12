import math
import tkinter as tk

allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}


def evaluate(expr: str):
    """Evaluate a mathematical expression using only allowed names."""
    try:
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        raise ValueError(f"Invalid expression {expr}: {e}")


def cli_mode():
    """Run the traditional command-line calculator."""
    print("Scientific Calculator. Type 'quit' to exit.")
    while True:
        try:
            expr = input(">>> ")
        except EOFError:
            break
        if expr.lower() in {"quit", "exit"}:
            break
        if not expr.strip():
            continue
        try:
            result = evaluate(expr)
            print(result)
        except Exception as e:
            print("Error:", e)


def ui_mode():
    """Launch a simple Tkinter based UI for the calculator."""
    root = tk.Tk()
    root.title("Scientific Calculator")

    entry = tk.Entry(root, width=40)
    entry.pack(padx=10, pady=10)

    result_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_var)
    result_label.pack(padx=10, pady=(0, 10))

    def evaluate_expr(event=None):
        expr = entry.get()
        if expr.lower() in {"quit", "exit"}:
            root.destroy()
            return
        if not expr.strip():
            result_var.set("")
            return
        try:
            result = evaluate(expr)
            result_var.set(str(result))
        except Exception as e:
            result_var.set(f"Error: {e}")

    calculate_btn = tk.Button(root, text="Calculate", command=evaluate_expr)
    calculate_btn.pack(padx=10, pady=(0, 10))

    entry.bind("<Return>", evaluate_expr)

    root.mainloop()


def main():
    mode = input("Select mode - 'cli' for command line or 'ui' for graphical (default cli): ").strip().lower()
    if mode == "ui":
        ui_mode()
    else:
        cli_mode()


if __name__ == "__main__":
    main()
