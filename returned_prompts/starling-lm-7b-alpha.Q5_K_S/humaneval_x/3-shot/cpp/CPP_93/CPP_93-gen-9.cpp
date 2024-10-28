    string result;
    char chr;
    int i;
    for (i=0;i<message.length();i++)
    {
        chr=toupper(message[i]);
        if (chr>='A' && chr<='Z')
        {
            if (chr=='A')
            result+='Y';
            if (chr=='B')
            result+='Z';
            if (chr=='C')
            result+='X';
            if (chr=='D')
            result+='W';
            if (chr=='E')
            result+='V';
            if (chr=='F')
            result+='U';
            if (chr=='G')
            result+='T';
            if (chr=='H')
            result+='S';
            if (chr=='I')
            result+='R';
            if (chr=='J')
            result+='Q';
            if (chr=='K')
            result+='P';
            if (chr=='L')
            result+='O';
            if (chr=='M')
            result+='N';
            if (chr=='N')
            result+='M';
            if (chr=='O')
            result+='L';
            if (chr=='P')
            result+='K';
            if (chr=='Q')
            result+='J';
            if (chr=='R')
            result+='I';
            if (chr=='S')
            result+='H';
            if (chr=='T')
            result+='G';
            if (chr=='U')
            result+='F';
            if (chr=='V')
            result+='E';
            if (chr=='W')
            result+='D';
            if (chr=='X')
            result+='C';
            if (chr=='Y')
            result+='B';
            if (chr=='Z')
            result+='A';
        }
        else
        {
            chr=tolower(message[i]);
            if (chr=='a')
            result+