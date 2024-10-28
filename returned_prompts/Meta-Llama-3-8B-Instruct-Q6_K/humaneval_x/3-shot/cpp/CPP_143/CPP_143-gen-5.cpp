    string result = "";
    string words[sentence.length()];
    int i;
    int j;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i] == ' ')
        {
            words[j++] = &sentence[i-1];
        }
    }
    for (i=0;i<j;i++)
    {
        if (isPrime(strlen(words[i])))
        {
            result += words[i];
        }
    }
    return result;
}

bool isPrime(int n)
{
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}