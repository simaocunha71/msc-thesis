    vector<string> even_list;
    for(auto &str: lst){
        if(str.length() % 2 == 0)
            even_list.push_back(str);
    }
    sort(even_list.begin(), even_list.end());
    return even_list;
}


