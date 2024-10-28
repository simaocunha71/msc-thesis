
def make_a_pile(n):
    ans = []
    num = n
    while num > 0:
        if num % 2 == 0:
            ans.append(num)
        else:
            ans.append(num+1)
        num -= 1
    return ans

# These "asserts" using only for self-checking and not necessary.
if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-v":
        print(make_a_pile(3))
        print(make_a_pile(5))
        print(make_a_pile(10))
        print(make_a_pile(20))















# Here are some tests for this problem. You can add your own.
if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        assert make_a_pile(3) == [3, 5, 7], "make_a_pile(3)"
        assert make_a_pile(5) == [5, 7, 9, 11, 13], "make_a_pile(5)"
        assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28], "make_a_pile(10)"
        assert make_a_pile(20) == [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58], "make_a_pile(20)"
        print("success!")
































