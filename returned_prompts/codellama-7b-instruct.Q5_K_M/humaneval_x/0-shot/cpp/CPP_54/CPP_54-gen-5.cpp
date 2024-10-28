    for(int i = 0; i < s0.size(); i++){
        for(int j = 0; j < s1.size(); j++){
            if(s0[i] == s1[j]){
                s0.erase(i, 1);
                s1.erase(j, 1);
                i--;
                j--;
                goto A;
            }
        }
    }
    if(s0.empty() == true && s1.empty() == true){
        return true;
    }
    else{
        return false;
    }
}
int main()
{
    string s0, s1;
    cin >> s0;
    cin >> s1;
    bool ans = same_chars(s0, s1);
    cout << (ans ? "true" : "false") << endl;
    return 0;
}
