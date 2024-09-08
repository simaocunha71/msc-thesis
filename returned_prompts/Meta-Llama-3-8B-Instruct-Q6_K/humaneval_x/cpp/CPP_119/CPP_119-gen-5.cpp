    if(lst[0][0] == '(' && lst[1][0] == ')'){
        return "Yes";
    }
    if(lst[0][0] == ')' && lst[1][0] == '('){
        return "No";
    }
    if(lst[0][0] == '(' && lst[1][0] == '('){
        return match_parens({lst[0].substr(1), lst[1]});
    }
    if(lst[0][0] == ')' && lst[1][0] == ')'){
        return match_parens({lst[0], lst[1].substr(1)});
    }
    return match_parens({lst[0].substr(1), lst[1]});
}
int main() {
    vector<string> lst = { "()(", ")" };
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}
B:
    string match_parens(vector<string> v) {
        int open = 0, close = 0;
        for (int i = 0; i < v[0].size(); i++) {
            if (v[0][i] == '(') open++;
            else close++;
        }
        for (int i = 0; i < v[1].size(); i++) {
            if (v[1][i] == '(') open++;
            else close++;
        }
        if ((open == close) && (open == 0 || close == 0)) return "Yes";
        return "No";
    }
    int main() {
        vector<string> v = {"()(", ")"};
        cout << match_parens(v) << endl;
        return 0;
    }
C:
    string match_parens(vector<string> v) {
        int open = 0, close = 0;
        for (int i = 0; i < v[0].size(); i++) {
            if (v[0][i] == '(') open++;
            else close++;
        }
        for (int i = 0; i < v[1].size(); i++) {
            if (v[1][i] == '(') open++;
            else close++;
        }
        if ((open == close) && (open == 0 || close == 0)) return "Yes";
        return "No";
    }
    int main() {
        vector<string> v = {"()