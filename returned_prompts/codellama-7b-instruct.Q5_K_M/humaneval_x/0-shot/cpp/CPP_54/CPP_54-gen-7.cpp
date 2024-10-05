
    for(int i=0;i<s0.size();i++){
        for(int j=0;j<s1.size();j++){
            if(s0[i]==s1[j]){
                s0.erase(i,1);
                s1.erase(j,1);
                goto A;
            }
        }
    }
    if(s0.size()==0&&s1.size()==0){
        return true;
    }else{
        return false;
    }
}
int main(){
    string s0,s1;
    cin>>s0>>s1;
    bool ans=same_chars(s0,s1);
    cout<<ans<<endl;
    return 0;
}

