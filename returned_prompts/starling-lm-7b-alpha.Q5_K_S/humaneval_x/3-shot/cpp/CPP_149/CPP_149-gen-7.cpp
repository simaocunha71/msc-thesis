    vector<string> even_list;
    vector<string> odd_list;
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    even_list.push_back(lst[i]);
    else
    odd_list.push_back(lst[i]);
    sort(odd_list.begin(),odd_list.end());
    sort(even_list.begin(),even_list.end(),[](string a,string b){return a.length()<b.length();});
    odd_list.insert(odd_list.end(),even_list.begin(),even_list.end());
    return odd_list;
}

