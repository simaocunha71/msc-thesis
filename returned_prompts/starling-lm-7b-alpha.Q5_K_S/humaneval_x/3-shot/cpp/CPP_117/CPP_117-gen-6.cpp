    vector<string> cons_words;
    char chr;
    char consonants[]={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
    int i,j,count;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        count=0;
        for (j=0;j<consonants[j]!=chr;j++)
        if (chr==consonants[j])
        count+=1;
        if (count==n)
        cons_words.push_back(s.substr(i));
    }
    return cons_words;
}


