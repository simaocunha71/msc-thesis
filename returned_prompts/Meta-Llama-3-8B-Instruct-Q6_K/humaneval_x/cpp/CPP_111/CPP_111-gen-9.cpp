    map<char,int> result;
    for(string::iterator it = test.begin(); it != test.end(); ++it)
    {
        if(result.find(*it) == result.end())
        {
            result[*it] = 1;
        }
        else
        {
            result[*it]++;
        }
    }
    int maxCount = 0;
    for(map<char,int>::iterator it = result.begin(); it != result.end(); ++it)
    {
        if(it->second > maxCount)
        {
            maxCount = it->second;
        }
    }
    map<char,int> maxMap;
    for(map<char,int>::iterator it = result.begin(); it != result.end(); ++it)
    {
        if(it->second == maxCount)
        {
            maxMap[it->first] = it->second;
        }
    }
    return maxMap;
}

int main()
{
    string test = "a b c";
    map<char,int> result = histogram(test);
    for(map<char,int>::iterator it = result.begin(); it != result.end(); ++it)
    {
        printf("(%c, %d)\n",it->first,it->second);
    }
    return 0;
}
