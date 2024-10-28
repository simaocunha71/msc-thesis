    string binary="";
    int i;
    int temp;
    temp=decimal;
    binary+="db";
    while(temp>0)
    {
        if(temp%2==0)
        binary+="0";
        else
        binary+="1";
        temp=temp/2;
    }
    binary+="db";
    string new_binary="";
    for (i=binary.length()-1;i>=0;i--)
    new_binary+=binary[i];
    return new_binary;
}

