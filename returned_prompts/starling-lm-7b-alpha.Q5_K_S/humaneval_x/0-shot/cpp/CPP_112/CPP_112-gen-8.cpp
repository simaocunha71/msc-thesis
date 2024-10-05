    string s_rev = s;
    reverse(s_rev.begin(), s_rev.end());
    for(int i=0;i<s.size();i++)
        for(int j=0;j<c.size();j++)
            if(s[i]==c[j]){
                s.erase(i,1);
                s_rev.erase(s_rev.size()-i-1,1);
                break;
            }
    vector<string> ans;
    ans.push_back(s);
    ans.push_back(s_rev);
    return ans;
}

vector<string> delete_(string s,string c){
    for(int i=0;i<s.size();i++)
        for(int j=0;j<c.size();j++)
            if(s[i]==c[j]) s.erase(i,1);
    vector<string> ans;
    ans.push_back(s);
    return ans;
}

string rev(string s){
    string ans;
    for(int i=s.size()-1;i>=0;i--) ans.push_back(s[i]);
    return ans;
}

vector<string> reverse_delete_(string s,string c){
    for(int i=0;i<s.size();i++)
        for(int j=0;j<c.size();j++)
            if(s[i]==c[j]){
                s.erase(i,1);
                break;
            }
    vector<string> ans;
    ans.push_back(s);
    ans.push_back(rev(s));
    return ans;
}

int main(){
    string s,c;
    cin>>s>>c;
    vector<string> ans;
    ans = reverse_delete(s,c);
    if(ans[0]==ans[1]) cout<<"True";
    else cout<<"False";
    return 0;
}























