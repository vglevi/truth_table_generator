from scripts.text_to_forms import infix_to_rnp, get_variables, get_forms

from collections import deque
import unittest

class TestRPN(unittest.TestCase):
    def test_infix_to_rnp(self):
        self.assertEqual(infix_to_rnp("A & B"), deque(["A", "B", "&"]))
        self.assertEqual(infix_to_rnp("(A & B)"), deque(["A", "B", "&"]))
        self.assertEqual(infix_to_rnp("(A) & (B)"), deque(["A", "B", "&"]))
        self.assertEqual(infix_to_rnp("A -> B"), deque(["A", "B", "->"]))
        self.assertEqual(infix_to_rnp("A - B"), deque(["A-B"]))
        self.assertEqual(infix_to_rnp("A <-> B"), deque(["A", "B", "<->"]))
        self.assertEqual(infix_to_rnp("A <--> B"), deque(["A<-", "B", "->"]))
        self.assertEqual(infix_to_rnp("~A & B"), deque(["A", "~", "B", "&"]))
        self.assertEqual(infix_to_rnp("~(A & B)"), deque(["A", "B", "&", "~"]))
        self.assertEqual(infix_to_rnp("~(A) & B"), deque(["A", "~", "B", "&"]))
        self.assertEqual(infix_to_rnp("A & B | C"), deque(["A", "B", "&", "C", "|"]))
        self.assertEqual(infix_to_rnp("A & (B | C)"), deque(["A", "B", "C", "|", "&"]))
        self.assertEqual(infix_to_rnp("A & (B | (C -> D))"), deque(["A", "B", "C", "D", "->", "|", "&"]))

    def test_get_variables(self):
        self.assertEqual(get_variables(deque(["A", "B", "C", "D", "->", "|", "&"])), ["A", "B", "C", "D"])
        self.assertEqual(get_variables(deque(["ab", "~", "cd", "&"])), ["ab", "cd"])

    def test_get_forms(self):
        self.assertDictEqual(get_forms(deque(["A", "B", "C", "D", "->", "|", "&"]),
                                       {'A': "T", 'B': "F", 'C': "F", 'D': "T"}),
                             {'A': "T", 'B': "F", 'C': "F", 'D': "T",
                              'C -> D': "T", 'B | (C -> D)': "T", 'A & (B | (C -> D))': "T"})

if __name__ == "__main__":
    unittest.main()
