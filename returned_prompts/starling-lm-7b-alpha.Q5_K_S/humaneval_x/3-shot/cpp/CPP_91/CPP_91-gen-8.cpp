    int i,j,count=0;
    string current_word;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.'||S[i]=='?'||S[i]=='!')
        {
            j=i;
            while (S[j]!='.')
            {
                j++;
            }
            j--;
            if (S[j]=='I'&&S[j-1]==' '){
                count++;
            }
            i=j;
        }
    }
    return count;
}


