    int count=0;
    for(int i=1; i<s.length(); i+=2){
        if(isupper(s[i]) && s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U'){
            count++;
        }
    }
    return count;
}
int main(){
    string s;
    cout<<"Enter the string: "<<endl;
    cin>>s;
    cout<<"The number of uppercase vowels in even indices is: "<<count_upper(s)<<endl;
    return 0;
}
