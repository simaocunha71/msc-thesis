    int cnt=0;
    char vowels[] = {'A', 'E', 'I', 'O', 'U'};
    for(int i=0; i<s.length(); i+=2){
        if(find(begin(vowels), end(vowels), s[i]) != end(vowels))
            cnt++;
    }
    return cnt;
}


