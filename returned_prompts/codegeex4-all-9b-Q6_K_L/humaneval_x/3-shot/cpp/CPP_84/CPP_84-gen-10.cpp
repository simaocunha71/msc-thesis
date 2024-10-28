    string result;
    int number=N;
    int remainder;
    while (number>0)
    {
        remainder=number%2;
        result=to_string(remainder)+result;
        number=number/2;
    }
    return result;
}

