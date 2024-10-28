    if (n>m)
    return "-1";
    float average=0;
    int i;
    for (i=n;i<=m;i++)
    average+=i;
    average=average/(m-n+1);
    int rounded=round(average);
    string binary_string=to_string(rounded);
    return binary_string;
}



