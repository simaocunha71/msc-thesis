    vector<int> result;
    sort(lst.begin(), lst.end());
    for (int i=0; i<lst.size(); i+=2){
        if (i+1<lst.size())
        result.push_back(lst[i]);
        else
        result.push_back(lst[i]);
    }
    return result;
}