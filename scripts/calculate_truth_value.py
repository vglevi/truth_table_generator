import itertools


def generate_truth_scenarios(var_num: int):
    return list(itertools.product("TF", repeat=var_num))

def assign_variable_values(variables: list, values: tuple):
    variables_with_values = {}
    for i, var in enumerate(variables):
        variables_with_values[var] = values[i]
    return variables_with_values

def calculate_truth_value(variable_values: dict, operator: str, variables: list[str]):
    values = []
    for var in variables:
        while var.startswith("(") and var.endswith(")"):
            var = var[1:-1]
        if variable_values[var] == "T":
            values.append(True)
        else:
            values.append(False)
    if operator == "~":
        if values[0]:
            return "F"
        else:
            return "T"
    elif operator == "&":
        if values[0] and values[1]:
            return "T"
        else:
            return "F"
    elif operator == "|":
        if values[0] or values[1]:
            return "T"
        else:
            return "F"
    elif operator == "->":
        if (not values[0]) or values[1]:
            return "T"
        else:
            return "F"
    elif operator == "<->":
        if (values[0] and values[1]) or ((not values[0]) and (not values[1])):
            return "T"
        else:
            return "F"
