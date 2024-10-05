    int i;
    int size=word.size();
    for (i=size-1;i>0;i--)
    {
        if (word[i]>='a' && word[i]<='z')
        {
            if (word[i-1]>='A' && word[i-1]<='Z')
            {
                return word[i];
            }
        }
    }
    return "";
}


