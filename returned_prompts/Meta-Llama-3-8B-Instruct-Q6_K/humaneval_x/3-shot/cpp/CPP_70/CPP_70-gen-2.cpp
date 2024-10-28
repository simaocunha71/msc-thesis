    vector<int> result;
    vector<int> temp=lst;
    while (!temp.empty())
    {
        int min_val=min_element(temp.begin(),temp.end())->operator*();
        result.push_back(min_val);
        temp.erase(remove(temp.begin(),temp.end(),min_val),temp.end());
        if (!temp.empty())
        {
            int max_val=max_element(temp.begin(),temp.end())->operator*();
            result.push_back(max_val);
            temp.erase(remove(temp.begin(),temp.end(),max_val),temp.end());
        }
    }
    return result;
}
