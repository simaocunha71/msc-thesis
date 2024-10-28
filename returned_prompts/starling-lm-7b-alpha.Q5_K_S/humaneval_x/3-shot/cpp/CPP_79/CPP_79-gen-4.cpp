    string binary="";
    string temp="";
    int i,j;
    for (i=0;i<10;i++)
    {
        temp+='0';
    }

    binary="db"+temp;
    i=temp.size()-1;
    while (decimal>0)
    {
        binary[i]='1'+'0'-decimal%2;
        decimal/=2;
        i--;
    }
    binary+="db";
    return binary;
}



