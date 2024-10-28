    string vowels={"a","e","i","o","u"};
    string result;
    int i;
    for (i=0;i<text.length();i++)
    if (!(find(vowels.begin(),vowels.end(),tolower(text[i]))!=vowels.end()))
    result+=text[i];
    return result;
}


