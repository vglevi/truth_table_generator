from collections import deque

def infix_to_rnp(text: str):
    operator_precedence = {"~": 0, "&": 1, "|": 2, "->": 3, "<->": 4}
    text = text.replace(" ", "")

    stack = []
    queue = deque()

    i = 0
    operand = ""
    while i < len(text):
        operator = ""
        if text[i] in {"~", "&", "|"}:
            operator = text[i]
        elif text[i] == "-":
            if text[i + 1] == ">":
                operator = "->"
            else:
                operand += text[i]
        elif text[i] == "<":
            if text[i+1 : i+3] == "->":
                operator = "<->"
            else:
                operand += text[i]
        
        elif text[i] not in {"(", ")"}:
            operand += text[i]

        if operator:
            if operand:
                queue.append(operand)
                operand = ""
            while stack and stack[-1] != "(" and operator_precedence[stack[-1]] < operator_precedence[text[i]]:
                queue.append(stack.pop())
            stack.append(operator)
            i += len(operator)
            continue

        if text[i] == "(":
            if operand:
                queue.append(operand)
                operand = ""
            stack.append(text[i])
        elif text[i] == ")":
            if operand:
                queue.append(operand)
                operand = ""
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()

        i += 1
    
    if operand:
        queue.append(operand)

    while stack:
        queue.append(stack.pop())

    return queue


