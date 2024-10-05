    int min_val;
    vector<int> strange_lst;
    int i;
    if (lst.size()==0)
    return strange_lst;
    min_val=*min_element(lst.begin(), lst.end());
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]==min_val)
        {
            strange_lst.push_back(min_val);
            lst.erase(lst.begin()+i);
            i-=1;
        }
    }
    int max_val=*max_element(lst.begin(), lst.end());
    strange_lst.push_back(max_val);
    lst.erase(remove(lst.begin(), lst.end(), max_val),lst.end());
    i=lst.size();
    for (i=0;i<lst.size();i++)
    {
        min_val=*min_element(lst.begin(), lst.end());
        strange_lst.push_back(min_val);
        lst.erase(lst.begin()+i);
        i-=1;
    }
    return strange_lst;
}


