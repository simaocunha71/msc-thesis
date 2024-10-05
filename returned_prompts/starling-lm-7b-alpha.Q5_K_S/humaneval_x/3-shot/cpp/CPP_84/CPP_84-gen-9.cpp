    string binary="";
    int i;
    int tmp;
    for (i=0;i<4;i++)
    {
        tmp=N%2;
        binary+=to_string(tmp);
        N/=2;
    }
    reverse(binary.begin(),binary.end());
    return binary;
}




