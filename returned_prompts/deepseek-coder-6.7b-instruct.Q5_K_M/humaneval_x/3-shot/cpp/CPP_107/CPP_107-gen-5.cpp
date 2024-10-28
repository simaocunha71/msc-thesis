    int i, j;
    string s;
    int even_count = 0;
    int odd_count = 0;
    vector<int> res(2, 0);
    for(i = 1; i <= n; i++){
        s = to_string(i);
        if(s == string(s.rbegin(), s.rend())){
            if(s.length() % 2 == 0)
                even_count++;
            else
                odd_count++;
        }
    }
    res[0] = even_count;
    res[1] = odd_count;
    return res;
}


