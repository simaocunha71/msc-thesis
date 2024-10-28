    string s="",pre="",post="";
    int len=str.length();
    for (int i=0;i<len;i++){
        if (is_palindrome(str.substr(i))){
            post=str.substr(i);
            break;
        }
    }
    for (int i=len-1;i>=0;i--){
        if (is_palindrome(str.substr(0,i))){
            pre=str.substr(0,i);
            break;
        }
    }
    s=pre+post;
    reverse(s.begin(),s.end());
    return s;
}



