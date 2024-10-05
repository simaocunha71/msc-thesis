    for(int i=0;i<s.size();i++){
        if(s[i]>='a'&&s[i]<='z'){
            s[i]=s[i]-'a'+'A';
        }else if(s[i]>='A'&&s[i]<='Z'){
            s[i]=s[i]-'A'+'a';
        }
    }
    for(int i=0;i<s.size();i++){
        if(!(s[i]>='a'&&s[i]<='z')){
            s[i]=(s[i]-'0')*10+(s[i]=='-'?-1:1);
        }
    }
    int i=0,j=s.size()-1;
    while(i<j){
        char tmp=s[i];
        s[i]=s[j];
        s[j]=tmp;
        i++;j--;
    }
    return s;
}

int main(){
    string s;
    cin>>s;
    cout<<solve(s);
}















































































































































































































































