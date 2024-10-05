    string words[100];
    int i=0;
    int j=0;
    int k=0;
    int flag=0;
    int num_words=0;
    int prime_words=0;
    int len_words=0;
    while (sentence[i]!='\0')
    {
        while (sentence[i]!=' ' && sentence[i]!='\0')
        {
            words[j][i] = sentence[i];
            i++;
            j++;
        }
        words[j][i] = '\0';
        j=0;
        i++;
        if (is_prime(len_words))
        {
            prime_words++;
        }
        len_words=0;
    }

    while (words[k][0]!='\0')
    {
        num_words++;
        k++;
    }

    if (prime_words==num_words)
    {
        return words;
    }
}

bool is_prime(int num)
{
    if (num==0 || num==1)
    {
        return false;
    }
    for (int i=2;i<num;i++)
    {
        if (num%i==0)
        {
            return false;
        }
    }
    return true;
}


