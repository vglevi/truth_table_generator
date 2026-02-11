from scripts.infix_to_rpn import infix_to_rnp

from collections import deque
import unittest

class TestRPN(unittest.TestCase):
    def test(self):
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

if __name__ == "__main__":
    unittest.main()
