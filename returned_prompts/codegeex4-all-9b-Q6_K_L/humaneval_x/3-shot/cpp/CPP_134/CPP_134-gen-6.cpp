    char last_char=txt[txt.size()-1];
    if (last_char==' '||last_char=='\0')
    return false;
    if (last_char>='a'&&last_char<='z')
    return true;
    if (last_char>='A'&&last_char<='Z')
    return true;
    return false;
}

