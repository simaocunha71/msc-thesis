    vector<int> tmp;
    vector<int> tmp2;
    vector<int> tmp3;
    for (int i : arr)
    if (i>=1 && i<=9) tmp.push_back(i);
    sort(tmp.begin(),tmp.end());
    reverse(tmp.begin(),tmp.end());

    for (int i : tmp)
    if (i!=0) tmp2.push_back(i);
    sort(tmp2.begin(),tmp2.end());
    reverse(tmp2.begin(),tmp2.end());

    for (int i : tmp2)
    if (i!=0) tmp3.push_back(i);
    sort(tmp3.begin(),tmp3.end());
    reverse(tmp3.begin(),tmp3.end());

    vector<string> result;
    for (int i : tmp3)
    result.push_back(map<int,string>({1="One", 2="Two", 3="Three", 4="Four", 5="Five", 6="Six", 7="Seven", 8="Eight", 9="Nine"})[i]);
    return result;
}


