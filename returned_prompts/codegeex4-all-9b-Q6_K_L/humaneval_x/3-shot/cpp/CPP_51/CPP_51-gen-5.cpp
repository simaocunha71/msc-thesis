    string vowels="aeiou";
    for (int i=0;i<text.length();i++)
    {
        char chr=text[i];
        if (vowels.find(chr)!=string::npos)
            text.erase(i,1);
    }
    return text;
}

