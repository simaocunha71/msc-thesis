    string vowels="AEIOUaeiou";
    int i,j,k;
    for (i=word.length()-1;i>=1;i--)
    {
        if (find(vowels.begin(),vowels.end(),word[i])!=vowels.end())
        {
            j=i+1;
            while (j<word.length()-1)
            {
                if (find(vowels.begin(),vowels.end(),word[j])==vowels.end())
                j++;
                else
                break;
            }
            if (j==word.length()-1)
            {
                k=i-1;
                while (k>=0)
                {
                    if (find(vowels.begin(),vowels.end(),word[k])==vowels.end())
                    k--;
                    else
                    break;
                }
                if (k==-1)
                return "";
                else
                return word[i];
            }
            else
            return "";
        }
    }
    return "";
}

