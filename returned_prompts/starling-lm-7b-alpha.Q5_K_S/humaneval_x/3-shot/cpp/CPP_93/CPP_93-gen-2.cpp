    string result;
    char chr;
    for (int i=0;i<message.length();i++)
    {
        chr=toupper(message[i]);
        if (chr=='A')
            result+='C';
        if (chr=='E')
            result+='G';
        if (chr=='I')
            result+='K';
        if (chr=='O')
            result+='Q';
        if (chr=='U')
            result+='W';
        if (chr=='Y')
            result+='A';
        if (chr<'A'||chr>'Z')
            result+=message[i];
    }
    return result;
}


