    int max=0;
    int sum=0;
    for (int i=0;i<lst.size();i++){
        int current=lst[i];
        if (current>max)
            max=current;
    }
    string s = to_string(max);
    for (int i=0;i<s.length();i++){
        sum+=s[i]-'0';
    }
    return sum;
}



