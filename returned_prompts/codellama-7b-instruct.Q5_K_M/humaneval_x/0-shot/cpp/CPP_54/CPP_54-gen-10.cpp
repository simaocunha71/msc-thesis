    if (s0.size()!=s1.size()){
        return false;
    }
    for (int i=0;i<s0.size();i++){
        for (int j=0;j<s1.size();j++){
            if (s0[i]==s1[j]){
                goto B;
            }
        }
        return false;
    }
B:
    if (i==s0.size()-1){
        return true;
    }
    else{
        i++;
        goto A;
    }
}
int main(){
    string s0,s1;
    cin>>s0>>s1;
    if (same_chars(s0,s1)){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}
