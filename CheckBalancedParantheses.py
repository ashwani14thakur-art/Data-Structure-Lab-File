def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return stack == []


expression = input("Enter an expression: ")

if is_balanced(expression):
    print("Parentheses are balanced.")
else:
    print("Parentheses are NOT balanced.")
