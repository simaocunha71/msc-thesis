    string result="";
    char chr;
    int i;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u' || chr=='A' || chr=='E' || chr=='I' || chr=='O' || chr=='U')
        continue;
        result+=chr;
    }
    return result;
}



