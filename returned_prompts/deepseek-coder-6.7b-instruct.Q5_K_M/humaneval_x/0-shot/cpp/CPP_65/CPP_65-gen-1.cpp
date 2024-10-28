
    int count = 0;
    int temp = x;
    while (temp != 0)
    {
        count++;
        temp = temp / 10;
    }

    if (shift > count)
    {
        string s = to_string(x);
        reverse(s.begin(), s.end());
        return s;
    }

    string str = to_string(x);
    str = str.substr(count - shift) + str.substr(0, count - shift);

    return str;
}

int main()
{
    printf("%s\n", circular_shift(12, 1).c_str());
    printf("%s\n", circular_shift(12, 2).c_str());
    return 0;
}

//C++/shift_digits_left.cpp
