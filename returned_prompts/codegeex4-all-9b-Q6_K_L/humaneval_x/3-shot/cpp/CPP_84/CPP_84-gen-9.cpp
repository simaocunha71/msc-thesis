    string binary="";
    int i,quotient=N;
    while (quotient>0)
    {
        if (quotient%2==0)
        {
            binary="0"+binary;
        }
        else
        {
            binary="1"+binary;
        }
        quotient=quotient/2;
    }
    return binary;
}

