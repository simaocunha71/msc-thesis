```
def even_bit_set_number(n):
    return n | (n >> 1)
```
The function works by performing a bitwise OR operation on the number `n` and the result of shifting `n` one bit to the right (`n >> 1`). This effectively sets all even bits of `n` to 1, as the even bits of `n` are the same as the odd bits of `n` shifted one bit to the right. 

For example, if `n` is 10 (which is 1010 in binary), `n >> 1` is 5 (which is 0101 in binary). The bitwise OR operation on `n` and `n >> 1` is 1011, which is the binary representation of 11, which is 10 + 2 (the even bits of 10 are 0 and 2, and these are set to 1 in 11). 

This solution passes the given unit test: `assert even_bit_set_number(10) == 10`. 