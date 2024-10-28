    int even_count=0, odd_count=0;
    for(int i=1;i<=n;i++){
        if(i<10){
            if(i%2==0) even_count++;
            else odd_count++;
        }
        else if(i<100){
            if(i%11==0) odd_count++;
        }
        else{
            string s=to_string(i);
            if(s[0]==s[2]) {
                if(s[0]%2==0) even_count++;
                else odd_count++;
            }
        }
    }
    return {even_count, odd_count};
}


