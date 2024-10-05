    int even = 0, odd = 0;
    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        string r = string(s.rbegin(), s.rend());
        if(s == r){
            if(s.length() % 2 == 0)
                even++;
            else
                odd++;
        }
    }
    return {even, odd};
}


