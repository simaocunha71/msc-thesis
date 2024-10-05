    int max_freq=0;
    int max_num=-1;
    map<int,int> freq;
    for (int i=0;i<lst.size();i++)
    {
        freq[lst[i]]++;
    }
    for (auto it=freq.begin();it!=freq.end();it++)
    {
        if (it->second>=it->first && it->first>0)
        {
            if (it->second>max_freq)
            {
                max_freq=it->second;
                max_num=it->first;
            }
        }
    }
    if (max_num>-1)
    return max_num;
    else
    return -1;
}
// Or in one line
int search(vector<int> lst){
    map<int,int> freq;
    for (int i=0;i<lst.size();i++)
    {
        freq[lst[i]]++;
    }
    for (auto it=freq.begin();it!=freq.end();it++)
    {
        if (it->second>=it->first && it->first>0)
        return it->first;
    }
    return -1;
} 
// Or with std::max_element
int search(vector<int> lst){
    map<int,int> freq;
    for (int i=0;i<lst.size();i++)
    {
        freq[lst[i]]++;
    }
    return std::max_element(freq.begin(),freq.end(), 
    [&freq](auto a, auto b){
        if (a.second>=a.first && a.first>0 && b.second>=b.first && b.first>0)
        return a.second>b.second;
        else
        return a.second>b.second;
    })->first;
}
// Or with std::find_if
int search(vector<int> lst){
    map<int,int> freq;
    for (int i=0;i<lst.size();i++)
    {
        freq[lst[i]]++;
    }
    return std::find_if(freq.begin(),freq.end(), 
    [&freq](auto a){
        return a.second>=a.first && a.first>0;
    })->first;
}  // This will return the first element that satisfies the condition, if no such element exists, it will throw an exception. If you want to return -1 in such case, you can add a check before returning the value.  // This will return -1 if no such element exists.  int search(vector<int> lst){     map<int,int> freq;