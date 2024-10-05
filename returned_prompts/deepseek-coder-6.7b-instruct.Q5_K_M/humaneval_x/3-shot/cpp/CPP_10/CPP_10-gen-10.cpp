    if(is_palindrome(str)) return str;
    for(int i = str.size(); i >= 0; --i){
        if(is_palindrome(str.substr(0, i))){
            string s(str.rbegin()+i, str.rend());
            return str+string(s.rbegin(), s.rend());
        }
    }
}


