    int sum =0;
    int count =0;
    for(int i=0;i<s.length();i++){
        if(s[i]=='a'||s[i]=='o'){
            count++;
        }
        else if(s[i]=='m'){
            sum = sum + count;
            count = 0;
        }
    }
    return n - sum;
}
