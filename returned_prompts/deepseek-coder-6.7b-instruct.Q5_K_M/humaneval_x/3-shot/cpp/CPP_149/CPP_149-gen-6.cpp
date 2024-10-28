    vector<string> odd_strings;
    for(auto str : lst)
        if(str.size() % 2 == 0)
            odd_strings.push_back(str);

    sort(odd_strings.begin(), odd_strings.end());

    return odd_strings;
}

