    for(int i=0; i<str.length(); i++){
        if(str[i]>='a' && str[i]<='z'){
            str[i] = str[i] - 32;
        }
        else if(str[i]>='A' && str[i]<='Z'){
            str[i] = str[i] + 32;
        }
    }
    return str;
}
int main(){
    string str = "Hello";
    cout<<filp_case(str)<<endl;
    return 0;
}