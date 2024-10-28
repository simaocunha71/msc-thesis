    string ans;
    int i;
    int len;
    string word;
    len=sentence.length();
    for (i=0;i<len;i++)
    {
        if (sentence[i]==' ')
        {
            if (is_prime(word.length()))
            {
                ans+=word;
            }
            word="";
        }
        else
        {
            word+=sentence[i];
        }
    }
    return ans;
}

