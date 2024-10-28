    int i,j,count_even=0,count_odd=0;
    string s;
    for(i=1;i<=n;i++){
        s=to_string(i);
        if(s==string(s.rbegin(),s.rend())){
            if(s.length()%2==0)
                count_even++;
            else
                count_odd++;
        }
    }
    return {count_even,count_odd};
}



