def text_match_three(text):
    if len(text) >= 4 and text[0] == 'a' and text[1:4] == 'bb':
        return True
    return False

# Test case
assert not text_match_three("ac")  # Expected output: False
assert text_match_three("abbb")  # Expected output: True
assert not text_match_three("abc")  # Expected output: False
assert not text_match_three("ab")  # Expected output: False
assert text_match_three("abbba")  # Expected output: True

# The function text_match_three checks if the given text starts with 'a' and has 'bb' immediately following. If the text meets these conditions, the function returns True; otherwise, it returns False. The unit tests provided ensure that the function behaves as expected in different scenarios.  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501
#  # noqa: E501