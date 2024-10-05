    string vowels="aeiouAEIOU";
    int i,j;
    for (i=word.length()-1;i>=0;i--)
    if (vowels.find(word[i])!=string::npos)
    {
        for (j=i-1;j>=0;j--)
        if (vowels.find(word[j])!=string::npos)
        return word[i];
    }

    return "";
}



