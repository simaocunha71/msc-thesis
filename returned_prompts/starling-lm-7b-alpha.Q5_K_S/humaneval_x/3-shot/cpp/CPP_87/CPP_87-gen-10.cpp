    vector<vector<int>> result;
    vector<int>::iterator it;
    vector<vector<int>>::iterator it2;
    int i;
    for (i=0;i<lst.size();i++)
    {
        it=find(lst[i].begin(), lst[i].end(), x);
        if (it!=lst[i].end())
        {
            vector<int> new_vector;
            new_vector.push_back(i);
            new_vector.push_back(it-lst[i].begin());
            result.push_back(new_vector);
        }
    }

    sort(result.begin(), result.end());
    return result;
}




