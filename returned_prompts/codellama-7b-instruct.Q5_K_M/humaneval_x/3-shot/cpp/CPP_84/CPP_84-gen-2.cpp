    string binary;
    while (N>0)
    {
        binary+=N%2;
        N/=2;
    }
    int sum=0;
    for (int i=0;i<binary.length();i++)
    sum+=binary[i]-'0';
    return to_string(sum);
}


