
}

int main(){
    vector<string> lst = {"()(", ")"};
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}

*/

#include<iostream>
#include<vector>
#include<string>
using namespace std;

string match_parens(vector<string> lst){
    int open = 0, close = 0;
    for(int i=0; i<2; i++){
        for(int j=0; j<lst[i].size(); j++){
            if(lst[i][j] == '(') open++;
            else if(lst[i][j] == ')'){
                if(open > 0) open--;
                else close++;
            }
        }
    }
    return (open == close) ? "Yes" : "No";
}

int main(){
    vector<string> lst = {"()(", ")"};
    cout<< match_parens(lst)<<endl;
    return 0;
}

//test cases:
//match_parens({"()(", ")"}) --> "Yes"
//match_parens({")", ")"}) --> "No"
//match_parens({"((", "))"}) --> "Yes"
//match_parens({"()", "()"}) --> "Yes"
//match_parens({"(((", ")))("}) --> "No"
//match_parens({"()()", "()"}) --> "Yes"
//match_parens({"", "()()"}) --> "Yes"
//match_parens({"())(", "()"}) --> "Yes"
//match_parens({"())(", "(()"}) --> "No"
//match_parens({"()()()()()()()()()()()()()", "()"}) --> "Yes"
//match_parens({"()()()()()()()()()()()()(", ")"}) --> "No"
//match_parens({"((((