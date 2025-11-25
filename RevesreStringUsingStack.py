# Reverse a string using stack (simple version)

def reverse_using_stack(s):
    stack = []         

    for ch in s:
        stack.append(ch)

    rev = ""
    while stack:
        rev += stack.pop()

    return rev

text = input("Enter a string: ")         
print("Original String:", text)

reversed_text = reverse_using_stack(text)
print("Reversed String:", reversed_text)
