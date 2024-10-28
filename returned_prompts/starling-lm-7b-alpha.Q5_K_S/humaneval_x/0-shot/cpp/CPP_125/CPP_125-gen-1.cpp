    int cnt = 0;
    for(int i = 0; i < txt.length(); i++){
        if(txt[i] == ',' || txt[i] == ' '){
            cnt++;
        }
    }
    if(cnt == 0){
        char c;
        int count = 0;
        for(int i = 0; i < txt.length(); i++){
            c = txt[i];
            if(c >= 'a' && c <= 'z'){
                if((c - 'a') % 2 == 1){
                    count++;
                }
            }
        }
        vector<string> v;
        v.push_back(to_string(count));
        return v;
    }
    else{
        vector<string> v;
        for(int i = 0; i < txt.length(); i++){
            if(txt[i] == ',' || txt[i] == ' '){
                v.push_back("");
            }
            else{
                v[v.size() - 1] += txt[i];
            }
        }
        return v;
    }
}
int main(){
    string s;
    cin >> s;
    for(auto c : split_words(s)){
        cout << c << " ";
    }
    cout << endl;
}























































































































































































