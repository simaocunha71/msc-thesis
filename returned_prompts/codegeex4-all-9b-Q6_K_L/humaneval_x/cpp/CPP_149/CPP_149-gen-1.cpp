vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(int i=0;i<lst.size();i++)
    {
        int len=lst[i].length();
        if(len%2==0)
            result.push_back(lst[i]);
    }
    sort(result.begin(),result.end());
    return result;
}