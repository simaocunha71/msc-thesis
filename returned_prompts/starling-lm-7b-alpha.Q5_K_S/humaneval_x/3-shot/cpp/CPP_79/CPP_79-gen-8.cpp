    string binary="";
    int i;
    for (i=0;decimal>0;i++)
    {
        binary+=(decimal%2)+'0';
        decimal/=2;
    }
    return "db"+string(i,'0')+binary+"db";
}


