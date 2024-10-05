    string binary="";
    char chr;
    int i,j;
    for (i=15;i>=0;i--)
    {
        chr=(decimal>>i)&1;
        binary+=(chr==0?'0':'1');
    }
    binary+="db";
    for (i=0;i<binary.length();i++)
    if (binary[i]=='1')
    {
        for (j=0;j<i;j++)
        binary[j]=binary[j+1];
        binary[j]='0';
        break;
    }
    binary+="db";
    return binary;
}


