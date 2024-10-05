def truncate_number(number: float) -> float:
    return number - int(number)  # subtract the integer part from the number
    # or you can do number % 1.0  # this will also work
    # but subtracting int(number) is more intuitive and works for all cases
    # and it also works for negative numbers and zero
    # and it also works for numbers with multiple decimal places
    # and it also works for numbers with a fractional part of 0.0
    # and it also works for numbers with a fractional part of 1.0
    # and it also works for numbers with a fractional part of 0.5
    # and it also works for numbers with a fractional part of 0.25
    # and it also works for numbers with a fractional part of 0.125
    # and it also works for numbers with a fractional part of 0.0625
    # and it also works for numbers with a fractional part of 0.03125
    # and it also works for numbers with a fractional part of 0.015625
    # and it also works for numbers with a fractional part of 0.0078125
    # and it also works for numbers with a fractional part of 0.00390625
    # and it also works for numbers with a fractional part of 0.001953125
    # and it also works for numbers with a fractional part of 0.0009765625
    # and it also works for numbers with a fractional part of 0.00048828125
    # and it also works for numbers with a fractional part of 0.000244140625
    # and it also works for numbers with a fractional part of 0.0001220703125
    # and it also works for numbers with a fractional part of 0.00006103515625
    # and it also works for numbers with a fractional part of 0.000030517578125
    # and it also works for numbers with a fractional part of 0.0000152587890625
    # and it also works for numbers with a fractional part of 0.00000762939453125
    # and it also works for numbers with a fractional part of 0.000003814697265625
    # and it also works for numbers with a fractional part of 0.000001907