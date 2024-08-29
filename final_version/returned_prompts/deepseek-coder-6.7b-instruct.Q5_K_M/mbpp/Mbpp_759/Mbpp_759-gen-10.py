def is_decimal(s: str) -> bool:
    try:
        float(s)
        return s.count('.') == 1 and len(s.split('.')[1]) == 2
    except ValueError:
        return False

assert is_decimal('123.11')==True
assert is_decimal('123.111')==False
assert is_decimal('123.')==False
assert is_decimal('.11')==False
assert is_decimal('123')==False
assert is_decimal('123.1')==False
assert is_decimal('123.111')==False
assert is_decimal('123.111')==False
assert is_decimal('123.111')==False
assert is_decimal('123.111')==False
assert is_decimal('123.111')==False
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 1.6
<jupyter_code>
