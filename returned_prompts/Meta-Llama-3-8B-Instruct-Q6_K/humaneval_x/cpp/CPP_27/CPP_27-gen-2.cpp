    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z'){
            str[i]-='a'+'A';
        }
        else if(str[i]>='A' && str[i]<='Z'){
            str[i]-='A'+'a';
        }
    }
    return str;
}

int main(){
    string s="Hello";
    cout<<filp_case(s);
    return 0;
}
