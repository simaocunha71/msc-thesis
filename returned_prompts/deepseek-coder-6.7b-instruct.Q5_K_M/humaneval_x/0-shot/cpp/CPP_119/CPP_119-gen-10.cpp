
    string s1 = lst[0];
    string s2 = lst[1];
    int open1 = 0, close1 = 0, open2 = 0, close2 = 0;
    for(int i = 0; i < s1.size(); i++){
        if(s1[i] == '(') open1++;
        else close1++;
    }
    for(int i = 0; i < s2.size(); i++){
        if(s2[i] == '(') open2++;
        else close2++;
    }
    if(close1 < open1 && close2 < open2) return "No";
    if(close1 > open1) s1 += s2.substr(0, open2);
    else if(close2 > open2) s2 += s1.substr(0, open1);
    if(s1.size() - open1 == close1 && s2.size() - open2 == close2) return "Yes";
    return "No";
}

//main function for testing
int main(){
    vector<string> test = {"()(", ")"};
    printf("%s\n", match_parens(test).c_str());
    test = {")", ")"};
    printf("%s\n", match_parens(test).c_str());
    return 0;
}

*/

//src/solution_1657.cpp
/*
