    if(s0.empty() && s1.empty()) return true;
    else if(s0.empty() || s1.empty()) return false;
    else if(s0[0]==s1[0]){
        s0.erase(0,1);
        s1.erase(0,1);
        goto A;
    }
    else return false;
}
int main(){
    string s0,s1;
    cin>>s0>>s1;
    cout<<same_chars(s0,s1);
    return 0;
}

