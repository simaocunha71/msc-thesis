    vector<string> result;
    char chr;
    int i,j,counter;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            counter=0;
            for (j=i-1;j>=0;j--)
            {
                chr=s[j];
                if ('a'<=chr&&chr<='z')
                {
                    if (is_consonant(chr))
                    {
                        counter+=1;
                    }
                }
                if (counter==n)
                {
                    string word;
                    for (int k=j;k<=i;k++)
                    {
                        chr=s[k];
                        if (chr==' '||chr=='\0')
                        {
                            break;
                        }
                        word+=chr;
                    }
                    result.push_back(word);
                }
            }
        }
    }
    return result;
}

bool is_consonant(char chr)
{
    if ('a'<=chr&&chr<='z')
    {
        return !('e'<=chr&&chr<='o');
    }
    return false;
}



