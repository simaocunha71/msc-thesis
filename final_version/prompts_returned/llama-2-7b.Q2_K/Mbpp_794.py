"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
text_starta_endb = lambda s: (s.startswith('aa') and bool(s[-1].islower())) if s else False
def test():
    assert not text_starta_endb("aabb")

if __name__ == '__main__':
    test()