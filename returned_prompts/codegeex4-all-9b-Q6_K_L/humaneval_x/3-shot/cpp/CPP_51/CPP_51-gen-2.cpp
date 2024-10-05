    string vowels="aeiouAEIOU";
    string result="";
    int i;
    for (i=0;i<text.length();i++)
    {
        if (find(vowels.begin(),vowels.end(),text[i])==vowels.end())
            result+=text[i];
    }
    return result;
}

