    string encoded;
    char chr;
    for (int i=0;i<message.length();i++)
    {
        chr=message[i];
        if (chr=='a')
        {
            chr='B';
        }
        if (chr=='e')
        {
            chr='F';
        }
        if (chr=='i')
        {
            chr='L';
        }
        if (chr=='o')
        {
            chr='R';
        }
        if (chr=='u')
        {
            chr='V';
        }
        if (chr=='A')
        {
            chr='B';
        }
        if (chr=='E')
        {
            chr='F';
        }
        if (chr=='I')
        {
            chr='L';
        }
        if (chr=='O')
        {
            chr='R';
        }
        if (chr=='U')
        {
            chr='V';
        }
        if (chr>=97&&chr<=122)
        {
            chr-=32;
        }
        else if (chr>=65&&chr<=90