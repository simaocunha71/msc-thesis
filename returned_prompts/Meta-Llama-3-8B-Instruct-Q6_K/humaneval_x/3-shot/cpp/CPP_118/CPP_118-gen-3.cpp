    int i;
    for (i=word.length()-1;i>0;--i)
    {
        if (word[i]=='a' || word[i]=='e' || word[i]=='i' || word[i]=='o' || word[i]=='u')
        {
            for (int j=i-1;j>=0;--j)
            {
                if (word[j] !='a' && word[j] !='e' && word[j] !='i' && word[j] !='o' && word[j] !='u')
                {
                    return word.substr(j+1, i-j-1);
                }
            }
        }
    }
    return "";
}