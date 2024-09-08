    vector<int> res;
    string str = to_string(abs(num));
    int even = 0, odd = 0;
    for(int i = 0; i < str.length(); i++){
        if(str[i] % 2 == 0)
            even++;
        else
            odd++;
    }
    res.push_back(even);
    res.push_back(odd);
    return res;
}

