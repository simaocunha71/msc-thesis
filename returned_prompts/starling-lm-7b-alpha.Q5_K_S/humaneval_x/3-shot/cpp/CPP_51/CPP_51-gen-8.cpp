    string no_vowels;
    char chr;
    for (int i=0;i<text.length();i++)
    {
        chr=tolower(text[i]);
        if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u')
        no_vowels+=chr;
    }
    return no_vowels;
}


