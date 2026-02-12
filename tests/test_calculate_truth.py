from scripts.calculate_truth_value import generate_truth_scenarios, assign_variable_values, calculate_truth_value

import unittest

class TestCalculate(unittest.TestCase):
    def test_generate_truth_scenarios(self):
        self.assertListEqual(generate_truth_scenarios(2), [("T", "T"), ("T", "F"), ("F", "T"), ("F", "F")])
        self.assertListEqual(generate_truth_scenarios(1), [("T",), ("F",)])

    def test_assing_variable_values(self):
        self.assertDictEqual(assign_variable_values(["A", "B", "C"], ("T", "F", "T")),
                                                    {"A": "T", "B": "F", "C": "T"})
        self.assertDictEqual(assign_variable_values(["A", "B"], ("F", "F")), {"A": "F", "B": "F"})

    def test_calc_truth(self):
        self.assertEqual("F", calculate_truth_value({"A": "T"}, "~", ["A"]))
        self.assertEqual("T", calculate_truth_value({"A": "T", "B": "T"}, "&", ["A", "B"]))
        self.assertEqual("T", calculate_truth_value({"A": "F", "B": "T"}, "|", ["A", "B"]))
        self.assertEqual("F", calculate_truth_value({"A": "T", "B": "F"}, "->", ["A", "B"]))
        self.assertEqual("T", calculate_truth_value({"A": "F", "B": "F"}, "<->", ["A", "B"]))
