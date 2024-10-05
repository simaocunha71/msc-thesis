

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


print(encode_shift("hello"))
print(decode_shift(encode_shift("hello")))
<jupyter_output>
mjqqt
hello
<jupyter_text>
Q2:
<jupyter_code>
