    string binary="";
    int i,sum=0,digit;
    for (i=0;i<5;i++)
    {
        digit=N%2;
        sum+=digit;
        binary+=(char)(digit+'0');
        N/=2;
    }
    if (sum==0) return "0";
    return string(binary.rbegin(),binary.rend());
}


