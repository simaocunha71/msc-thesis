    string result="";
    char chr;
    char chr2;
    int i;
    for (i=0;i<message.length();i++)
    {
        chr=toupper(message[i]);
        chr2=toupper(chr);
        if (chr2=='A')
        {
        chr2='C';
        }
        if (chr2=='E')
        {
        chr2='G';
        }
        if (chr2=='I')
        {
        chr2='K';
        }
        if (chr2=='O')
        {
        chr2='Q';
        }
        if (chr2=='U')
        {
        chr2='W';
        }
        if (chr2=='Y')
        {
        chr2='Z';
        }
        result+=chr2;
    }
    return result;
}


