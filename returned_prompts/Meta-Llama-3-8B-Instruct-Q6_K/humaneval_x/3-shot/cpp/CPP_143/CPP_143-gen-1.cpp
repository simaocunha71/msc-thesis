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

    string result;
    for (i=0;i<words.size();i++)
    {
        int len=words[i].length();
        if (isPrime(len))
        {
            result+=words[i]+" ";
        }
    }
    result.pop_back();
    return result;
}

bool isPrime(int n){
    if (n<2)
        return false;
    for (int i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return false;
    return true;
}