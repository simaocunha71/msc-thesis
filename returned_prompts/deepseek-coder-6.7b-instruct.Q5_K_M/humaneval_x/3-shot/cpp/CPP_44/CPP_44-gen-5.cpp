    string result="";
    int rest;
    while(x>0){
        rest=x%base;
        x=x/base;
        result=to_string(rest)+result;
    }
    return result;
}

