    int i=0,j;
    int n=word.length();
    char c;
    while (i<n)
    {
        c=word[i];
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
        {
            if (i==0)
            {
                return "";
            }
            else
            {
                for (j=i-1;j>=0;j--)
                {
                    c=word[j];
                    if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
                    {
                        return word[j];
                    }
                }
            }
        }
        i++;
    }
    return "";
}


