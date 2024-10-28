    string result="";
    char chars[]={'0','1','2','3','4','5','6','7','8','9'};
    while(x>0){
    result+=chars[x%base];
    x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}



