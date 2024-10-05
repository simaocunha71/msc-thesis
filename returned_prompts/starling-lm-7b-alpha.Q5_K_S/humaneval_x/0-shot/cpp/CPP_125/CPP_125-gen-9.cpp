    int n = txt.length();
    int i = 0;
    string s = "";
    vector<string> v;
    while(i < n){
        if(txt[i] == ' ' || txt[i] == ','){
            v.push_back(s);
            s = "";
        }else{
            s += txt[i];
        }
        i++;
    }
    v.push_back(s);
    return v;
}
vector<int> solve(string txt){
    int n = txt.length();
    int i = 0;
    int cnt = 0;
    vector<int> v;
    while(i < n){
        if(txt[i] != ' ' && txt[i] != ',' && txt[i] >= 'a' && txt[i] <= 'z'){
            if((txt[i] - 'a') % 2 == 1){
                cnt++;
            }
        }
        i++;
    }
    if(cnt == 0){
        v.push_back(26);
    }else{
        v.push_back(cnt);
    }
    return v;
}
int main(){
    string txt;
    cin >> txt;
    vector<string> v = split_words(txt);
    for(int i = 0; i < v.size(); i++)
        printf("%s ", v[i].c_str());
    printf("\n");
    vector<int> ans = solve(txt);
    for(int i = 0; i < ans.size(); i++)
        printf("%d ", ans[i]);
    printf("\n");
    return 0;
}










































































































