    string binary;
    string bin;
    while (N>0)
    {
        int remainder=N%2;
        binary=to_string(remainder)+binary;
        N=N/2;
    }
    return binary;
}



