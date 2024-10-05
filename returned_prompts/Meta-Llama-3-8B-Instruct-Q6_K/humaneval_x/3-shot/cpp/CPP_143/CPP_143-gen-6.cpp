    vector<string> words;
    string word;
    stringstream s(sentence);
    while (s >> word)
    {
        words.push_back(word);
    }
    string result;
    for (int i=0;i<words.size();i++)
    {
        if (is_prime(words[i].length()))
        result+=words[i]+" ";
    }
    return result.substr(0,result.length()-1);
}

bool is_prime(int n)
{
    if(n <= 1)
        return false;
    if(n == 2)
        return true;
    if(n % 2 == 0)
        return false;
    for(int i = 3; i <= sqrt(n); i += 2)
        if(n % i == 0)
            return false;
    return true;
}

