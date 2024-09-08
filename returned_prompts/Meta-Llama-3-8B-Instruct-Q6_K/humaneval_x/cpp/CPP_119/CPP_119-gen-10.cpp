    int i = 0, j = 0, open = 0, close = 0;
    while(i < lst[0].size() || j < lst[1].size()){
        if(i < lst[0].size() && lst[0][i] == '('){
            open++;
            i++;
        }
        else if(i < lst[0].size() && lst[0][i] == ')'){
            if(open > 0) open--;
            else return "No";
            i++;
        }
        else if(j < lst[1].size() && lst[1][j] == '('){
            open++;
            j++;
        }
        else if(j < lst[1].size() && lst[1][j] == ')'){
            if(open > 0) open--;
            else return "No";
            j++;
        }
    }
    if(open == 0) return "Yes";
    else return "No";
}

int main()
{
    vector<string> lst;
    lst.push_back("(");
    lst.push_back(")");
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}
B:
    string match_parens(vector<string> lst) {
        int open = 0, close = 0;
        for (char c : lst[0] + lst[1]) {
            if (c == '(') open++;
            else if (c == ')') {
                if (open > 0) open--;
                else return "No";
            }
        }
        return open == 0 ? "Yes" : "No";
    }
int main() {
    vector<string> lst;
    lst.push_back("(");
    lst.push_back(")");
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}
C:
    string match_parens(vector<string> lst) {
        int open = 0, close = 0;
        for (char c : lst[0]) {
            if (c == '(') open++;
            else if (c == ')') close++;
        }
        for (char c : lst[1]) {
            if (c == '(') close++;
            else if (c == ')') open++;
        }
        return open == close ? "Yes" : "No";
    }
int main() {
    vector<string> lst;
    lst.push_back("(");
    lst.push_back(")");
    printf("%