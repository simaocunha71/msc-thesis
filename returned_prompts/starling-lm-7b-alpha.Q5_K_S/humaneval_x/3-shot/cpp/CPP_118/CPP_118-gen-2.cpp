    string vowels="aeiouAEIOU";
    int i;
    for (i=0;i<word.length();i++)
    if (vowels.find(word[i])!=-1)
    return word[i];

    for (i=word.length()-2;i>=0;i--)
    if (vowels.find(word[i])!=-1)
    return word[i];

    return "";
}


