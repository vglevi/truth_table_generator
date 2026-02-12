from collections import deque

from scripts.calculate_truth_value import assign_variable_values, generate_truth_scenarios
from scripts.text_to_forms import get_forms, get_variables


def create_header(forms: dict):
    delimeter_line = "+"
    form_line = "┆"

    for form in forms:
        delimeter_line += "-" * (len(form) + 2) + "+"
        form_line += " " + form + " ┆"

    print(delimeter_line)
    print(form_line)
    print(delimeter_line)
    return delimeter_line

def create_table(rpn: deque):
    variables = get_variables(rpn)
    truth_scenarios = generate_truth_scenarios(len(variables))
    var_values = assign_variable_values(variables, truth_scenarios[0])
    forms = get_forms(rpn, var_values)

    delimeter_line = create_header(forms)

    line = "┆"
    for form in forms:
        left_space_num = (len(form) + 2) // 2
        right_space_num = (len(form) + 1) - left_space_num
        line += left_space_num * " " + forms[form] + right_space_num * " " + "┆"

    print(line)
    for i in range(1, len(truth_scenarios)):
        var_values = assign_variable_values(variables, truth_scenarios[i])
        forms = get_forms(rpn, var_values)
        line = "┆"
        for form in forms:
            left_space_num = (len(form) + 2) // 2
            right_space_num = (len(form) + 1) - left_space_num
            line += left_space_num * " " + forms[form] + right_space_num * " " + "┆"
        print(line)
    print(delimeter_line)
