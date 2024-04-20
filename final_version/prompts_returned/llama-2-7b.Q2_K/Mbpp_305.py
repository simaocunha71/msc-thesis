"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
import unittest
from utils import start_withp

def test0():
    assert start_withp(['Python php', 'java javascript'] == ('python', 'javascript'))

class TestStartWithP(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
if __name__=="__main__":
    test0()