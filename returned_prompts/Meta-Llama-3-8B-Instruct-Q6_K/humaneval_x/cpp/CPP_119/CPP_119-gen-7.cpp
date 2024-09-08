    int open = 0;
    int close = 0;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == '('){
                open++;
            }
            else if(lst[i][j] == ')'){
                close++;
            }
        }
    }
    if(open == close){
        return "Yes";
    }
    else{
        return "No";
    }
}
