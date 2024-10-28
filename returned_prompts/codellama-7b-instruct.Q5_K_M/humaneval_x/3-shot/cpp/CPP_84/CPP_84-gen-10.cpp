    string binary=to_string(N);
    string sum="";
    int i;
    for (i=0;i<binary.length();i++)
    {
        if (binary[i]=='1')
        sum+="1";
        else sum+="0";
    }
    return sum;
}


