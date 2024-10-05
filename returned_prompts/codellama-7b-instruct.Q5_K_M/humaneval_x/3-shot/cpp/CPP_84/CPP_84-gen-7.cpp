    string binary_string=to_string(N);
    int sum=0;
    for (int i=0;i<binary_string.length();i++)
    sum+=binary_string[i]-'0';
    return to_string(sum);
}



