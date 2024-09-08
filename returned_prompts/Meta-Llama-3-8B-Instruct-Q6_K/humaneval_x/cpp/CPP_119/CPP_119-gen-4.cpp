    if(lst.size()!=2)
        return "No";
    string s1 = lst[0];
    string s2 = lst[1];
    int count1 = 0;
    int count2 = 0;
    for(int i = 0; i < s1.size(); i++){
        if(s1[i] == '(')
            count1++;
        else
            count1--;
    }
    for(int i = 0; i < s2.size(); i++){
        if(s2[i] == '(')
            count2++;
        else
            count2--;
    }
    if(count1 == count2)
        return "Yes";
    else
        return "No";
}
int main()
{
    vector<string> lst1 = { "()(", ")" };
    vector<string> lst2 = {")", ")"};
    cout << match_parens(lst1) << endl;
    cout << match_parens(lst2) << endl;
    return 0;
}
