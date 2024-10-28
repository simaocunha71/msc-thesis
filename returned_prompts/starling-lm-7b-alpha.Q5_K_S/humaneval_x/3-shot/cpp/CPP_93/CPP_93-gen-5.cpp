    string encoded;
    char chr;
    char chr_next;
    int i;
    for (i=0;i<message.length();i++)
    {
        chr=tolower(message[i]);
        if (isupper(chr))
        {
            chr_next=toupper(chr+2);
            if (chr_next>'z')
            chr_next-=26;
        }
        else
        {
            chr_next=tolower(chr+2);
            if (chr_next>'z')
            chr_next-=26;
        }
        encoded+=chr_next;
    }
    return encoded;
}


