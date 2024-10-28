    int count=0;
    string word;
    int i=0;
    while(i<S.length())
    {
        while(i<S.length() && S[i]==' ')
        i++;
        if (i==S.length())
        break;
        int j=i;
        while(j<S.length() && S[j]!='.' && S[j]!='?' && S[j]!='!')
        j++;
        word=S.substr(i,j-i);
        i=j+1;
        if (word.substr(0,2)=="I ")
        count++;
    }
    return count;
}  // This code doesn't handle edge cases well. For example, it doesn't handle punctuation attached to a sentence.
