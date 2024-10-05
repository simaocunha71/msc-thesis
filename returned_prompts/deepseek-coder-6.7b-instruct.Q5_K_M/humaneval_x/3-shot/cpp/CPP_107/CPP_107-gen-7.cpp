    int even=0,odd=0;
    for(int i=1;i<=n;i++){
        string str = to_string(i);
        string rev = string(str.rbegin(), str.rend());
        if(str == rev){
            if(str.length() % 2 == 0)
                even++;
            else
                odd++;
        }
    }
    return {even, odd};
}


