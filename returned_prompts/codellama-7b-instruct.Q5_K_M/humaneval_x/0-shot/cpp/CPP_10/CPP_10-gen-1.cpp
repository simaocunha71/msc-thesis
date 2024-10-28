    string result;
    if(is_palindrome(str)){
        return str;
    }
    else{
        int suffix_index=0;
        while(str[suffix_index]==str[suffix_index+1]){
            suffix_index++;
        }
        int prefix_index=0;
        while(str[prefix_index]==str[suffix_index-prefix_index]){
            prefix_index++;
        }
        result=str.substr(0,prefix_index+1)+str.substr(suffix_index+1);
        result=str.substr(0,prefix_index+1)+string(result.rbegin(),result.rend())+str.substr(suffix_index+1);
        return result;
    }
}
int main(){
    string str;
    while(1){
        getline(cin,str);
        cout<<make_palindrome(str)<<endl;
    }
    return 0;
}
