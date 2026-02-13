from scripts.calculate_truth_value import calculate_truth_value

from collections import deque

operator_precedence = {"~": 0, "&": 1, "|": 2, "->": 3, "<->": 4}

def infix_to_rnp(text: str):
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
            while stack and stack[-1] != "(" and operator_precedence[stack[-1]] < operator_precedence[operator]:
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

    if "(" in queue or ")" in queue:
        raise Exception

    return queue

def get_variables(rnp: deque):
    return [v for v in rnp if v not in operator_precedence]

def get_forms(rnp: deque, variables_with_values: dict):
    forms = variables_with_values.copy()
    rpn = rnp.copy()
    stack = []
    while rpn:
        item = rpn.popleft()
        if item not in operator_precedence:
            stack.append(item)
        elif item == "~":
            a = stack.pop()
            form = f"~{a}"
            stack.append(form)
            forms[form] = calculate_truth_value(forms, item, [a])
        else:
            b = stack.pop()
            a = stack.pop()
            form = " ".join([a, item, b])
            stack.append(f"({form})")
            forms[form] = calculate_truth_value(forms, item, [a, b])

    return forms
