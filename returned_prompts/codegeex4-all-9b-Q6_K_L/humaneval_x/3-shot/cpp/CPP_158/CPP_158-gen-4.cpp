    int i,j,k,max=0,max_index=0;
    int counter[26];
    for (i=0;i<words.size();i++)
    {
        for (k=0;k<26;k++)
        counter[k]=0;
        for (j=0;j<words[i].length();j++)
        {
            counter[(int)words[i][j]-97]+=1;
        }
        for (k=0;k<26;k++)
        {
            if (counter[k]==1)
            {
            max+=1;
            }
        }
        if (max>max_index)
        {
            max_index=max;
            max=0;
        }
    }
    return words[max_index];
}

