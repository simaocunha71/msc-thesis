    map<char,int> result;
    string word;
    int i;
    for (i=0;i<test.length();i++)
    {
        word+=test[i];
        if (test[i]!=' ')
        {
            continue;
        }
        if (result.find(word[0])==result.end())
        {
            result[word[0]]=1;
        }
        else
        {
            result[word[0]]+=1;
        }
        word="";
    }
    return result;
}



