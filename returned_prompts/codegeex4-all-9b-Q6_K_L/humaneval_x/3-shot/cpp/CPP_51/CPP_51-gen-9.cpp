    string vowels="aeiouAEIOU";
    int i,j;
    for (i=0;i<text.size();i++)
    for (j=0;j<vowels.size();j++)
    if (text[i]==vowels[j])
    text.erase(i,1);
    return text;
}

