    string str = str;
    for (int i=str.length()-1;i>=0;i--)
    {
        if (is_palindrome(str.substr(0,i+1)))
            return str+string(str.rbegin(),str.rend()).substr(i+1);
    }
    return str+string(str.rbegin(),str.rend());
}
bool is_palindrome(string str){
    //Test if given string is a palindrome 
    string s(str.rbegin(),str.rend());
    return s==str;
}
int main(){
    cout<<make_palindrome("cata")<<endl;
    return 0;
}
