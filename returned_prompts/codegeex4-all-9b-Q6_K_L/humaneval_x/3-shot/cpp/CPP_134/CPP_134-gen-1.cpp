    if (txt.length()==0)
    return false;
    char chr=txt[txt.length()-1];
    return isalpha(chr) && txt[txt.length()-2]!=' ';
}