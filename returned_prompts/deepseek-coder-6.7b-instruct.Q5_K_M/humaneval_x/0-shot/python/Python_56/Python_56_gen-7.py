
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

#test_correct_bracketing.py
import unittest
from bracketing import correct_bracketing


class TestCorrectBracketing(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing("<"), False)
        self.assertEqual(correct_bracketing("<>"), True)
        self.assertEqual(correct_bracketing("<<><>>"), True)
        self.assertEqual(correct_bracketing("><<>"), False)
        self.assertEqual(correct_bracketing("<<><>>><<>><"), True)
        self.assertEqual(correct_bracketing("<<><>>><>><<"), False)


if __name__ == "__main__":
    unittest.main()

#test_correct_bracketing_v2.py
import unittest
from bracketing import correct_bracketing


class TestCorrectBracketing(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing("<"), False)
        self.assertEqual(correct_bracketing("<>"), True)
        self.assertEqual(correct_bracketing("<<><>>"), True)
        self.assertEqual(correct_bracketing("><<>"), False)
        self.assertEqual(correct_bracketing("<<><>>><<>><"), True)
        self.assertEqual(correct_bracketing("<<><>>><>><<"), False)
        self.assertEqual(correct_bracketing("<<><><>><>><<"), False)
        self.assertEqual(correct_bracketing("<<><><>>><><<"), False)
       