    int m=0;
    int n=0;
    for(int i=0;i<s0.length();i++){
        for(int j=0;j<s1.length();j++){
            if(s0[i]==s1[j]){
                m++;
                break;
            }
        }
    }
    for(int i=0;i<s1.length();i++){
        for(int j=0;j<s0.length();j++){
            if(s1[i]==s0[j]){
                n++;
                break;
            }
        }
    }
    if(m==s0.length()&&n==s1.length()){
        return true;
    }else{
        return false;
    }
}

int main(){
    string a="eabcdzzzz";
    string b="dddzzzzzzzddeddabc";
    printf("%d\n",same_chars(a,b));
    return 0;
}
