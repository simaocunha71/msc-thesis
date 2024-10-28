    int i,sum=0;
    string binary="";
    for (i=0;i<5;i++)
    {
    sum+=N%2;
    binary+=(char)(sum+'0');
    N/=2;
    }
    return binary.substr(binary.length()-5);
}


