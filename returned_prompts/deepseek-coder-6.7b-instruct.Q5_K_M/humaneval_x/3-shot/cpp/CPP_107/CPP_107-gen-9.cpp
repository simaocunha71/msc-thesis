    int even_count = 0;
    int odd_count = 0;
    for(int i=1; i<=n; i++){
        string str = to_string(i);
        string str_rev = string(str.rbegin(), str.rend());
        if(str == str_rev){
            if(str.length() % 2 == 0)
                even_count++;
            else
                odd_count++;
        }
    }
    return {even_count, odd_count};
}


