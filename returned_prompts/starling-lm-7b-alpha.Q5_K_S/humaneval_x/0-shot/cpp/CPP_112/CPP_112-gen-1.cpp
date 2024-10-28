vector<string>ans;
for(int i=0;i<s.size();i++){
    bool is_erased=false;
    for(int j=0;j<c.size();j++){
        if(s[i]==c[j]){
            is_erased=true;
        }
    }
    if(!is_erased){
        ans.push_back(string(1,s[i]));
    }
}

reverse(ans.begin(),ans.end());

vector<string>result;
result.push_back(ans[0]);
for(int i=1;i<ans.size();i++){
    result.push_back(ans[i]);
    result.push_back(ans[i]);
}
result.push_back(ans[ans.size()-1]);

if(is_palindrome(result)){
    ans.push_back("True");
}else{
    ans.push_back("False");
}

return ans;

}

bool is_palindrome(vector<string>s){
    int l=s.size();
    for(int i=0;i<l/2;i++){
        if(s[i]!=s[l-i-1]){
            return false;
        }
    }
    return true;
}

int main(){
    string s,c;
    cin>>s>>c;
    vector<string>ans=reverse_delete(s,c);
    for(int i=0;i<ans.size();i++){
        cout<<ans[i];
        if(i!=ans.size()-1){
            cout<<" ";
        }
    }
    cout<<endl;
}



*/




























































































