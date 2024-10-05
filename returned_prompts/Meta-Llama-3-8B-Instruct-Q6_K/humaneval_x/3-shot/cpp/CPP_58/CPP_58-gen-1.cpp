    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set<int> common;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),inserter(common,common.begin()));
    return vector<int>(common.begin(),common.end());
}
//or
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s;
    for(int i=0; i<l1.size(); i++)
        s.insert(l1[i]);
    for(int i=0; i<l2.size(); i++)
        if(s.find(l2[i]) != s.end())
            s.erase(s.find(l2[i]));
    vector<int> result(s.begin(),s.end());
    sort(result.begin(),result.end());
    return result;
} //This one is more efficient for large vectors


