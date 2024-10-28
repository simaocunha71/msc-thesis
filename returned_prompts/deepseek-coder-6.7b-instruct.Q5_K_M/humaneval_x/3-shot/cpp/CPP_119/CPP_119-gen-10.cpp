    int i;
    int count = 0;
    for(i = 0; i < lst[0].size(); i++){
        if(lst[0][i] == '(') count++;
        if(lst[0][i] == ')') count--;
        if(count < 0) return "No";
    }
    if(count != 0) return "No";
    count = 0;
    for(i = 0; i < lst[1].size(); i++){
        if(lst[1][i] == '(') count++;
        if(lst[1][i] == ')') count--;
        if(count < 0) return "No";
    }
    if(count != 0) return "No";
    return "Yes";
}


