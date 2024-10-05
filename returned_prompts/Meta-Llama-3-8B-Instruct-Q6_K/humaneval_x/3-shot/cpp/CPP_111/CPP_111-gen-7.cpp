    map<char,int> result;
    if (test.size()==0)
        return result;
    int max_count=0;
    for (int i=0;i<test.size();i++)
    {
        char chr=test[i];
        if (result.find(chr)!=result.end())
            result[chr]++;
        else
            result[chr]=1;
        if (result[chr]>max_count)
            max_count=result[chr];
    }
    map<char,int> temp;
    for (auto it=result.begin();it!=result.end();it++)
    {
        if (it->second==max_count)
            temp[it->first]=it->second;
    }
    return temp;
}
// This version of histogram uses a map to count the occurrences of each character,
// then iterates over the map to find the maximum count and creates a new map
// containing only the characters with that maximum count. It returns this new map.
// It also handles the case where the input string is empty by returning an empty map.
// The time complexity is O(n), where n is the length of the input string, because
// it iterates over the string once to count the occurrences and once to find the maximum count.
// The space complexity is O(n) as well, because in the worst case all characters in the
// string are different and thus we have to store all of them in the map.