    vector<string> v;
    string s1=s;
    sort(s1.begin(),s1.end());
    string s2=c;
    sort(s2.begin(),s2.end());
    while(s1.find(s2)!=s1.npos){
        s1.erase(s1.find(s2),1);
    }
    v.push_back(s1);
    return v;
}

vector<string> reverse_palindrome(string s,string c){

B:
    vector<string> v;
    string s1=s;
    reverse(s1.begin(),s1.end());
    v.push_back(s1);
    string s2="";
    for(int i=0;i<c.size();i++)s2+=c[i];
    reverse(s2.begin(),s2.end());
    while(s1.find(s2)!=s1.npos){
        s1.erase(s1.find(s2),1);
    }
    v.push_back(s1);
    return v;
}

int main(){
    string s,c;
    cin>>s>>c;
    vector<string> v=reverse_delete(s,c);
    v=reverse_palindrome(v[0],c);
    if(v[1]==v[0])cout<<"True"<<endl;
    else cout<<"False"<<endl;
    return 0;
}




















*/




























































































































