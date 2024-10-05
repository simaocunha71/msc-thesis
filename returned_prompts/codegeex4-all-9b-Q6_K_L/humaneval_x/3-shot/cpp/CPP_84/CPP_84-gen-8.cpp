    string str="";
    while (N>0)
    {
        str+=(N%2+'0');
        N/=2;
    }
    string str2="";
    for (int i=str.length()-1;i>=0;i--)
    {
        str2+=str[i];
    }
    return str2;
}

