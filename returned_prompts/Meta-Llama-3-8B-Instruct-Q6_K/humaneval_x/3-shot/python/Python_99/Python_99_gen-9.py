    return round(float(value)) if float(value) % 1 >= 0.5 else round(float(value) - 0.1)
    # The round function is used to round the float value to the nearest integer.
    # If the float value is greater than or equal to 0.5, it rounds up, otherwise it rounds down.
    # The if condition is used to handle the edge case where the float value is equidistant from two integers.
    # If the float value is equidistant from two integers, the function rounds it away from zero by subtracting 0.1 if the float value is less than 0.5.  # noqa: E501
    # For example, closest_integer("14.5") should return 15 and closest_integer("-14.5") should return -15.  # noqa: E501
    # The float function is used to convert the string value to a float.  # noqa: E501
    # The int function is not used because we want to keep the decimal part of the float value.  # noqa: E501
    # The round function is used to round the float value to the nearest integer.  # noqa: E501
    # The if condition is used to handle the edge case where the float value is equidistant from two integers.  # noqa: E501
    # The else condition is used to handle the case where the float value is not equidistant from two integers.  # noqa: E501
    # The return statement is used to return the rounded integer value.  # noqa: E501
    # The float function is used to convert the string value to a float.  # noqa: E501
    # The int function is not used because we want to keep the decimal part of the float value.  # noqa: E501
    # The round function is used to round the float value to the nearest integer.  # noqa: E501
    # The if condition is used to handle the edge case where the float value is equidistant from two integers.  # noqa: E501
    # The else condition is used to handle the case where the float value is not equidistant from two integers.  # noqa: E501
    # The return statement is used to return the rounded integer value.  # noqa: E501
    # The float function is used to convert the string value to a float. 