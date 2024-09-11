"""
def extract_quotation(s):
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            result.append(s[start:i])
            start = i + 1
    result.append(s[start:])
    return result
"""

def extract_quotation(s):
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            result.append(s[start+1:i])
            start = i + 1
    result.append(s[start:])
    return result


if __name__ == '__main__':
    print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))


# 这里是测试代码
import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])
        self.assertEqual(extract_quotation("It's 'time' to 'go'"), ['time', 'go'])
        self.assertEqual(extract_quotation("It's 'time' to 'go' and 'sleep'"), ['time', 'go', 'sleep'])
        self.assertEqual(extract_quotation("It's 'time' to 'go' and 'sleep' and 'eat'"), ['time', 'go', 'sleep', 'eat'])

if __name__ == '__main__':
    unittest.main()



"""
"""

def extract_quotation(s):
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            result.append(s[start+1:i])
            start = i + 1
    result.append(s[start:])
    return result


if __name__ == '__main__':
    print(extract_quotation('Cortex "A53"