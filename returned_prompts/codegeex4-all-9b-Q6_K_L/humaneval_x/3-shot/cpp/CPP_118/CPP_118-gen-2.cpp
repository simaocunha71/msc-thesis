    string vowels="aeiouAEIOU";
    string result="";
    int i;
    for (i=0;i<word.length();i++)
    {
        if (vowels.find(word[i])!=string::npos)
        result=word[i];
    }
    return result;
}

