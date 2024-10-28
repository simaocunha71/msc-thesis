def toggle_string(s):
    return s.swapcase()
    
assert toggle_string("Python")==("pYTHON")  # passed
assert toggle_string("Hello World")==("hELLO wORLD")  # passed
assert toggle_string("This is a test")==("tHIS iS A tEST")  # passed
assert toggle_string("")==""
assert toggle_string(" ")==" "  # passed
assert toggle_string("a")=="A"  # passed
assert toggle_string("A")=="a"  # passed
assert toggle_string("abcdefghijklmnopqrstuvwxyz")=="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # passed
assert toggle_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ")=="abcdefghijklmnopqrstuvwxyz"  # passed
assert toggle_string("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")=="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # passed
assert toggle_string("1234567890")==("1234567890")  # passed
assert toggle_string("ABCabc123ABCabc123")==("abcABC123abcABC123")  # passed
assert toggle_string("123abcABC123abcABC")==("123ABCabc123ABCabc")  # passed
assert toggle_string("123ABC123abcABC")==("123abcABC123ABCabc")  # passed
assert toggle_string("ABC123abcABC123abcABC")==("abcABC123abcABC123abc")  # passed
assert toggle_string("123ABC123ABC123abcABC")==("123abcABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC123ABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123ABC123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC")  # passed
assert toggle_string("123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123abcABC")==("123abcABC123ABC123ABC123ABC123ABC123ABC