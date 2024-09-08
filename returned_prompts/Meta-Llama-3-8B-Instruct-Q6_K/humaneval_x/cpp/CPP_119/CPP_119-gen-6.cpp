    string res = "";
    int count = 0;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == '('){
                res += '(';
                count++;
            }
            else if(lst[i][j] == ')'){
                if(count > 0){
                    res += ')';
                    count--;
                }
                else res += '(';
            }
        }
    }
    if(count == 0) return "Yes";
    else return "No";
}

