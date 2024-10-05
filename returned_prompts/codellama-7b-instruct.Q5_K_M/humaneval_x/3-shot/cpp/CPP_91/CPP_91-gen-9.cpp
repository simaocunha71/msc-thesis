    int i;
    int count=0;
    int j;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]=='!')
        {
            j=i-1;
            while (j>=0)
            {
                if (S[j]=='I')
                count+=1;
                j-=1;
            }
        }
    }
    return count;
}

