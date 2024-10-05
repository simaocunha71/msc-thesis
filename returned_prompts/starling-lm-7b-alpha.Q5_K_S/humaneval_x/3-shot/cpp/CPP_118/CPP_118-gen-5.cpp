    string vowel="AEIOUaeiou";
    int i,j;
    for (i=0;i<word.length();i++)
    if (vowel.find(word[i])!=-1)
    return word[i];

    for (i=word.length()-1;i>=0;i--)
    if (vowel.find(word[i])!=-1)
    return word[i];

    return "";
}



