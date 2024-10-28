    int even=0, odd=0;
    for(int i=1;i<=n;i++){
        string str = to_string(i);
        string str_rev = string(str.rbegin(), str.rend());
        if(str==str_rev){
            if(str.size()%2==0) even++;
            else odd++;
        }
    }
    return {even, odd};
}

