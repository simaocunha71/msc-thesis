    vector<string> even_lst;

    for(int i=0; i<lst.size(); i++)
        if(lst[i].size() % 2 == 0)
            even_lst.push_back(lst[i]);

    sort(even_lst.begin(), even_lst.end());

    return even_lst;
}

