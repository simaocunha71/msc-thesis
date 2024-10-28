    string result="";
    while (x>0){
        int remainder=x%base;
        x=x/base;
        result+=remainder+'0';
    }
    return result;
}



