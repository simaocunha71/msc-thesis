    int len = brackets.length();
    if(len == 0)
        return true;
    if(brackets[0] == '<'){
        brackets = brackets.substr(1,len-1);
        goto A;
    }
    else if(brackets[0] == '>'){
        brackets = brackets.substr(1,len-1);
        goto A;
    }
    return false;

}

