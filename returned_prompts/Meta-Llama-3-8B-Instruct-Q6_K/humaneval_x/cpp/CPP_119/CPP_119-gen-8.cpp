    // Check if the first string is good
    bool firstGood = true;
    int count = 0;
    for(int i = 0; i < lst[0].size(); i++){
        if(lst[0][i] == '(')
            count++;
        else if(lst[0][i] == ')'){
            if(count == 0)
                firstGood = false;
            else
                count--;
        }
    }
    if(!firstGood)
        return "No";
    
    // Check if the second string is good
    bool secondGood = true;
    count = 0;
    for(int i = 0; i < lst[1].size(); i++){
        if(lst[1][i] == '(')
            count++;
        else if(lst[1][i] == ')'){
            if(count == 0)
                secondGood = false;
            else
                count--;
        }
    }
    if(!secondGood)
        return "No";
    
    // Check if we can concatenate the strings to get a good string
    count = 0;
    for(int i = 0; i < lst[0].size() + lst[1].size(); i++){
        if(i < lst[0].size() && lst[0][i] == '(')
            count++;
        else if(i < lst[0].size() && lst[0][i] == ')'){
            if(count == 0)
                return "No";
            else
                count--;
        }
        else if(i >= lst[0].size() && lst[1][i-lst[0].size()] == '(')
            count++;
        else if(i >= lst[0].size() && lst[1][i-lst[0].size()] == ')'){
            if(count == 0)
                return "No";
            else
                count--;
        }
    }
    return "Yes";
}

int main(){
    vector<string> lst = { "()", ")" };
    cout << match_parens(lst) << endl;
    return 0;
}

Output:
No
