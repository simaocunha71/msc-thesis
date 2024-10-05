    int cnt = 0;
    string combined = lst[0] + lst[1];
    for(char c : combined){
        if(c == '(') cnt++;
        if(c == ')') cnt--;
        if(cnt < 0) return "No";
    }
    return cnt == 0 ? "Yes" : "No";
}


