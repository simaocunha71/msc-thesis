    int open = 0, close = 0;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == '(') open++;
            else close++;
        }
    }
    if (open == close) return "Yes";
    if (open > close) return "No";
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == '(') open--;
            else close--;
        }
    }
    if (open == 0) return "Yes";
    return "No";
}
int main(){
    vector<string> lst = { "()(", ")" };
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}
