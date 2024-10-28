    string binary_string;
    int level=0;
    int i;
    for (i=0;i<10;i++)
    {
        if (decimal%2==0)
        {
        binary_string+='0';
        decimal/=2;
        }
        else {
        binary_string+='1';
        decimal=(decimal/2)-1;
        }
    }
    binary_string="db"+binary_string+"db";
    return binary_string;
}


