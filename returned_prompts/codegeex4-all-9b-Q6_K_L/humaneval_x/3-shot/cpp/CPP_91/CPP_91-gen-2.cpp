    int i;
    int counter=0;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='I')
        {
            if (S[i+1]==' ')
            {
                counter+=1;
            }
        }
    }
    return counter;
}

