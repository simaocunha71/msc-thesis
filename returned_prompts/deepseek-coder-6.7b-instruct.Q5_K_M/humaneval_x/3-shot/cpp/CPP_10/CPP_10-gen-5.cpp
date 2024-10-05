    if(is_palindrome(str)) 
        return str;
    string rev(str.rbegin(), str.rend());
    for(size_t i=str.size(); i>=0; --i)
        if(is_palindrome(rev.substr(i))) 
            return str+string(str.begin(), str.begin()+i);
    return "";
}

