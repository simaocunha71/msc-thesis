    int i,j;
    int avg;
    int sum;
    string binary="";
    if (n>m)
    return "-1";

    avg=(n+m)/2;
    sum=(m-n+1)*avg;
    if (sum%2==0)
    {
    for (i=0;i<sum/2;i++)
    binary+='1';
    }
    else
    {
    for (i=0;i<(sum-1)/2;i++)
    binary+='1';
    binary+='0';
    }

    for (j=binary.length()-1;j>=0;j--)
    printf("%c",binary[j]);
    return binary;
}



