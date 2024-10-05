    string binary="db";
    for (int i=0;i<8;i++)
    {
        if (decimal>0)
        {
            binary+="0";
            decimal-=1;
        }
        else
        {
            binary+="1";
        }
    }
    binary+="db";
    return binary;
}


