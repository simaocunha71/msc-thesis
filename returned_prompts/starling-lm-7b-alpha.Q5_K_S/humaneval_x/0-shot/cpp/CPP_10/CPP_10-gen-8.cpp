    int i;
    string p,ans="";
    for(i=str.size()-1;i>=0;--i){
        p+=str[i];
        if(is_palindrome(p))
            break;
        if(i>=1)
            ans=str.substr(0,i)+ans+str.substr(i,str.size());
    }
    return str+ans+str.substr(0,i+1);
}

