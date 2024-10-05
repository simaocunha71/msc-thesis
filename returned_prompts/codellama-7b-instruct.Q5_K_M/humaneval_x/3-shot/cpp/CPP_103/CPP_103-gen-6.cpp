    int average=(n+m)/2;
    int rounded_average=round(average);
    if (n>m)
    return "-1";
    string binary;
    while (rounded_average)
    {
        binary+=rounded_average%2;
        rounded_average/=2;
    }
    return binary;
}


