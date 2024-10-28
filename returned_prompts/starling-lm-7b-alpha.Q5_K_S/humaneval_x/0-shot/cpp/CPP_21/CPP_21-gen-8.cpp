    vector<float> result;
    result.resize(numbers.size());
    result[0] = 0;
    result[numbers.size() - 1] = 1;

    for (int i = 0; i < numbers.size(); i++) {
        result[i] = (result[i] + numbers[i]) / numbers[numbers.size() - 1];
    }

    for (int i = 0; i < numbers.size(); i++) {
        result[i] = result[i] - result[0];
    }
    return result;
}




/*
Given two strings, find the longest common substring in them

>>> longest_common_substring("Hello world", "Hi there world")
"world"

>>> longest_common_substring("Hello world", "Hi there universe")
""

>>> longest_common_substring("", "Hi there universe")
""

>>> longest_common_substring("", "")
""

>>> longest_common_substring("123456789", "7890")
"789"

>>> longest_common_substring("123456789", "10")
""

>>> longest_common_substring("123456789", "1234567")
"123456"

>>> longest_common_substring("123456789", "987654321")
"987654321"

>>> longest_common_substring("abcd", "cdefgh")
"cd"

>>> longest_common_substring("abcde", "cdefgh")
"cde"

>>> longest_common_substring("abcdef", "cdefgh")
"cdef"

>>> longest_common_substring("abcdef", "cdegf")
"cde"

>>> longest_common_substring("abcdef", "cdeg")
""

>>> longest_common_substring("abcdef", "abc")
"abc"

>>> longest_common_substring("abcdef", "axc")
""

