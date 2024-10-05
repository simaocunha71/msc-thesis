    string binary;
    int i;
    for (i=0;i<8;i++)
    {
        if ((decimal>>i)&1)
        {
            binary='1'+binary;
        }
        else
        {
            binary='0'+binary;
        }
    }
    return "db"+binary+"db";
}   // 8 bits is the default for integer in C++


