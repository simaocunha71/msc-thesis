    string vowels="aeiou";
    for (int i=0;i<vowels.length();i++)
    {
        char chr=vowels[i];
        while (text.find(chr)!=string::npos)
        {
            text.erase(text.find(chr),1);
        }
    }
    return text;
}


