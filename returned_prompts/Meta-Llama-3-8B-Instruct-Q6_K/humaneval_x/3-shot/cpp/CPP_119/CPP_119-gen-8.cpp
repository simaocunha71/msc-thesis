    int open=0;
    int close=0;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]=='(')
                open++;
            else
                close++;
        }
    }
    if ((open==close)||(open==close+1))
        return "Yes";
    else
        return "No";
} 
//Test
int main(){
    vector<string> lst1 = {"()(", ")"};
    vector<string> lst2 = {")", ")"};
    printf("%s\n", match_parens(lst1).c_str());
    printf("%s\n", match_parens(lst2).c_str());
    return 0;
} 

