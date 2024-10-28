    int level = 0;
    char chr;
    int i, j;
    for(i=0; i<2; i++){
        for(j=0; j<lst[i].length(); j++){
            chr = lst[i][j];
            if(chr == '('){
                level += 1;
            }
            if(chr == ')'){
                level -= 1;
                if(level < 0){
                    return "No";
                }
            }
        }
    }
    if(level == 0){
        return "Yes";
    }
    return "No";
}

