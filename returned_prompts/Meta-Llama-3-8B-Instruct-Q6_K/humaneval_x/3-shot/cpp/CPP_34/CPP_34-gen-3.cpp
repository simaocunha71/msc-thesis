    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        bool found=false;
        for (int j=0;j<result.size();j++)
        {
            if (l[i]==result[j])
            {
                found=true;
                break;
            }
        }
        if (!found)
        {
            result.push_back(l[i]);
        }
    }
    sort(result.begin(),result.end());
    return result;
} 
//or 
vector<int> unique(vector<int> l){
    set<int> s(l.begin(), l.end());
    vector<int> result(s.begin(), s.end());
    sort(result.begin(), result.end());
    return result;
} 
//or 
vector<int> unique(vector<int> l){
    sort(l.begin(),l.end());
    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        if (i==0 || l[i]!=l[i-1])
        {
            result.push_back(l[i]);
        }
    }
    return result;
} 

