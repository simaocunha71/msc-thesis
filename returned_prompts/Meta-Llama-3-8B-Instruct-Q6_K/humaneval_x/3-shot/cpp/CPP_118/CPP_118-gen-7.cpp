    int i;
    for (i=word.size()-1;i>=0;i--)
    {
        if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'||word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U')
        {
            for (int j=i-1;j>=0;j--)
            {
                if (isalpha(word[j]))
                {
                    if (isalpha(word[j+1]))
                    {
                        return word.substr(j+1, i-j-1);
                    }
                }
            }
        }
    }
    return "";
} 

