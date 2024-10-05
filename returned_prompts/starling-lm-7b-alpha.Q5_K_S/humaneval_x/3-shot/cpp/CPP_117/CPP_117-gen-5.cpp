    vector<string> result;
    vector<string>::iterator it;
    char chr;
    int i,j;
    string word;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
        if (word.length()>0)
        {
            int count=0;
            for (j=0;j<word.length();j++)
            {
            if (!isvowel(word[j]))
            {
            count+=1;
            }
            }
            if (count==n)
            {
            result.push_back(word);
            }
        }

        word="";
        }
        else
        {
        word+=chr;
        }
    }
    if (word.length()>0)
    {
    int count=0;
    for (j=0;j<word.length();j++)
    {
    if (!isvowel(word[j]))
    {
    count+=1;
    }
    }
    if (count==n)
    {
    result.push_back(word);
    }
    }
    return result;
}

bool isvowel(char chr)
{
    if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u')
    return true;
    return false;
}



