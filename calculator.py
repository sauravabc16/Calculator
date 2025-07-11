import math

allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}


def evaluate(expr: str):
    """Evaluate a mathematical expression using only allowed names."""
    try:
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        raise ValueError(f"Invalid expression {expr}: {e}")


def main():
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


if __name__ == "__main__":
    main()
