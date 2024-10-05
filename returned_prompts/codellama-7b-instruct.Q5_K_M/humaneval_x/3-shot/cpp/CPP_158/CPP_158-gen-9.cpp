    sort(words.begin(),words.end());
    int max=words[0].length();
    int i;
    int j;
    for (i=1;i<words.size();i++)
    if (words[i].length()>max)
    {
        max=words[i].length();
        j=i;
    }
    return words[j];
}


