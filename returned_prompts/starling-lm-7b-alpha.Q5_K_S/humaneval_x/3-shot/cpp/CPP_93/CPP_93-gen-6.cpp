    char chr;
    char new_chr;
    char original_chr;
    string encoded_message="";
    for (int i=0;i<message.length();i++)
    {
        chr=toupper(message[i]);
        if (isalpha(chr))
        {
            if (chr=='A')
                new_chr='C';
            else if (chr=='B')
                new_chr='D';
            else if (chr=='C')
                new_chr='E';
            else if (chr=='D')
                new_chr='F';
            else if (chr=='E')
                new_chr='G';
            else if (chr=='F')
                new_chr='H';
            else if (chr=='G')
                new_chr='I';
            else if (chr=='H')
                new_chr='J';
            else if (chr=='I')
                new_chr='K';
            else if (chr=='J')
                new_chr='L';
            else if (chr=='K')
                new_chr='M';
            else if (chr=='L')
                new_chr='N';
            else if (chr=='M')
                new_chr='O';
            else if (chr=='N')
                new_chr='P';
            else if (chr=='O')
                new_chr='Q';
            else if (chr=='P')
                new_chr='R';
            else if (chr=='Q')
                new_chr='S';
            else if (chr=='R')
                new_chr='T';
            else if (chr=='S')
                new_chr='U';
            else if (chr=='T')
                new_chr='V';
            else if (chr=='U')
                new_chr='W';
            else if (chr=='V')
                new_chr='X';
            else if (chr=='W')
                new_chr='Y';
            else if (chr