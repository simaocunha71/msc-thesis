    balanced = 0
    groups = []
    group = ''
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            balanced += 1
            group += paren_string[i]
        elif paren_string[i] == ')':
            balanced -= 1
            group += paren_string[i]
        else:
            group += paren_string[i]
        if balanced == 0:
            groups.append(group)
            group = ''
            balanced = 1
    return groups


class TestSeparateParenGroups(unittest.TestCase):
    def test_1(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
    def test_2(self):
        self.assertEqual(separate_paren_groups('()'), ['()'])
    def test_3(self):
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])
    def test_4(self):
        self.assertEqual(separate_paren_groups('((())) ()'), ['((()))', '()'])
    def test_5(self):
        self.assertEqual(separate_paren_groups('((())) (())'), ['((()))', '(())'])
    def test_6(self):
        self.assertEqual(separate_paren_groups('((())) (( ))'), ['((()))', '((()))'])
    def test_7(self):
        self.assertEqual(separate_paren_groups('() () ()'), ['()', '()', '()'])
    def test_8(self):
        self.assertEqual(separate_paren_groups('() (()) ()'), ['()', '(())', '()'])
    def test_9(self):
        self.assertEqual(separate_paren_groups('() (()) (())'), ['()', '(())', '(())'])
    def test_10(self):
        self.assertEqual(separate_