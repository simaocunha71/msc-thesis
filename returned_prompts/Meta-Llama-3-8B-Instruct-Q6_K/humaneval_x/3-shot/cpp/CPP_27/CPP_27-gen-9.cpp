    string result;
    for (char chr : str)
    {
        if (chr>=97 && chr<=122)
            result+=chr-32;
        else if (chr>=65 && chr<=90)
            result+=chr+32;
        else
            result+=chr;
    }
    return result;
}