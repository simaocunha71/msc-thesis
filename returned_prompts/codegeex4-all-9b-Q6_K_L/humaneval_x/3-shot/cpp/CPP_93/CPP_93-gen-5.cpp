    string encoded;
    int i=0;
    for (i=0;i<message.length();i++)
    {
        char chr=message[i];
        if (chr>='a' && chr<='z')
        {
            if (chr=='a')
            chr='C';
            if (chr=='e')
            chr='G';
            if (chr=='i')
            chr='K';
            if (chr=='o')
            chr='Q';
            if (chr=='u')
            chr='W';
            if (chr>='b' && chr<='c')
            chr-=2;
            if (chr>='d' && chr<='f')
            chr-=2;
            if (chr>='g' && chr<='h')
            chr-=2;
            if (chr>='j' && chr<='k')
            chr-=2;
            if (chr>='l' && chr<='m')
            chr-=2;
            if (chr>='n' && chr<='p')
            chr-=2;
            if (chr>='r' && chr<='s')
            chr-=2;
            if (chr>='t' && chr<='v')
            chr-=2;
            if (chr>='w' && chr<='z')
            chr-=2;
        }
        if (chr>='A' && chr<='Z')
        {
            if (chr=='A')
            chr='C';
            if (chr=='E')
            chr='G';
            if (chr=='I')
            chr='K';
            if (chr=='O')
            chr='Q';
            if (chr=='U')
            chr='W';
            if (chr>='B' && chr<='C')
            chr-=2;
            if (chr>='D' && chr<='F')
            chr-=2;
            if (chr>='G' && chr<='H')
            chr-=2;
            if (chr>='J' && chr<='K')
            chr-=2;
            if (chr>='L' && chr<='M')
            chr-=2;
            if (chr>='N' && chr<='P')
            chr-=2;
            if (chr>='R' && chr<='S')
            chr-=2;
            if (chr>='T' && chr<='V')
            chr-=2;
            if (chr>