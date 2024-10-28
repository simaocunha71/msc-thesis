def decimal_to_binary(n):
    return bin(n)[2:]  # [2:] to remove the '0b' prefix
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(256) == '10000000'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(0) == ''
assert decimal_to_binary(-1) == '-1'  # test for negative number
assert decimal_to_binary(-256) == '-10000000'  # test for negative number
assert decimal_to_binary(0.5) == '0.1'  # test for non-integer
assert decimal_to_binary(1.5) == '1.1'  # test for non-integer
assert decimal_to_binary(-0.5) == '-0.1'  # test for non-integer
assert decimal_to_binary(-1.5) == '-1.1'  # test for non-integer
assert decimal_to_binary(0.5e2) == '0.1'  # test for non-integer with exponent
assert decimal_to_binary(1.5e2) == '1.1'  # test for non-integer with exponent
assert decimal_to_binary(-0.5e2) == '-0.1'  # test for non-integer with exponent
assert decimal_to_binary(-1.5e2) == '-1.1'  # test for non-integer with exponent
assert decimal_to_binary(0.5e-2) == '0.01'  # test for non-integer with negative exponent
assert decimal_to_binary(1.5e-2) == '1.01'  # test for non-integer with negative exponent
assert decimal_to_binary(-0.5e-2) == '-0.01'  # test for non-integer with negative exponent
assert decimal_to_binary(-1.5e-2) == '-1.01'  # test for non-integer with negative exponent
assert decimal_to_binary(-0) == ''  # test for negative zero
assert decimal_to_binary(-0.0) == ''  # test for negative zero
assert decimal_to_binary(0.0) == ''  # test for positive zero
assert decimal_to_binary(0.0e0) == ''  # test for positive zero
assert decimal_to_binary(0.0e-0) == ''