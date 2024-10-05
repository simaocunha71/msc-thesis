    int i=str.length()-1;
    while(i>=0 && is_palindrome(str.substr(0,i+1))){
        i--;
    }
    return str.substr(0,i+1)+str.substr(0,i+1).substr(0,str.length()-i-1);
}
int main(){
    string str="";
    cout<<"Enter a string: ";
    cin>>str;
    cout<<"Palindromized string: "<<make_palindrome(str);
    return 0;
}
