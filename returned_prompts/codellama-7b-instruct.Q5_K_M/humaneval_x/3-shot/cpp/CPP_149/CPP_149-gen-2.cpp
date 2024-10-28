    vector<string> sorted_list;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i].length()%2==0)
        {
            sorted_list.push_back(lst[i]);
        }
    }
    sort(sorted_list.begin(),sorted_list.end());
    return sorted_list;
}


