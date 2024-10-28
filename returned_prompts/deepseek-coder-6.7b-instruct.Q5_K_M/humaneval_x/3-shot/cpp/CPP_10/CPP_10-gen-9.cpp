    if(is_palindrome(str))
    return str;
    string rev(str.rbegin(),str.rend());
    for(int i=str.size()-1;i>=0;i--){
        if(is_palindrome(str.substr(0,i+1))){
            return str+rev.substr(rev.size()-i-1);
        }
    }
    return "";
}

