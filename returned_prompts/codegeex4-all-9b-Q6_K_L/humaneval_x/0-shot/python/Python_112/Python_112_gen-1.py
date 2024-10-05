def reverse_delete(s,c):
    for i in c:
        s = s.replace(i,'')
    if s == s[::-1]:
        return (s,True)
    return (s,False)

def test_reverse_delete():
    assert reverse_delete("abcde","ae") == ('bcd', False)
    assert reverse_delete("abcdef","b") == ('acdef', False)
    assert reverse_delete("abcdedcba","ab") == ('cdedc', True)
    assert reverse_delete("abccba","ab") == ('cc', True)
    assert reverse_delete("abccba","abc") == ('', False)
    assert reverse_delete("abccba","ac") == ('bcb', False)
    assert reverse_delete("abccba","abcd") == ('', False)
    assert reverse_delete("abccba","abcde") == ('', False)
    assert reverse_delete("abccba","") == ('abccba', False)
    assert reverse_delete("","") == ('', False)
    assert reverse_delete("","a") == ('', False)
    assert reverse_delete("a","") == ('a', False)
    assert reverse_delete("a","a") == ('', False)
    assert reverse_delete("abccba","abccba") == ('', False)
    assert reverse_delete("abccba","abccbaa") == ('', False)

print("All tests passed.")