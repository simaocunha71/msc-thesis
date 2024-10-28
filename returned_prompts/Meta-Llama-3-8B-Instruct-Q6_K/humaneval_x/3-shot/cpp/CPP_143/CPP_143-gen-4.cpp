    string result;
    vector<string> words;
    string word;
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            words.push_back(word);
            word="";
        }
        else
        {
            word+=sentence[i];
        }
    }
    words.push_back(word);
    for (i=0;i<words.size();i++)
    {
        int len=words[i].length();
        if (isPrime(len))
        {
            result+=words[i]+" ";
        }
    }
    return result.substr(0,result.length()-1);
}

bool isPrime(int n)
{
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;

    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;

    return true;
}