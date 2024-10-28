    string result="";
    while(x>0){
        result+=char(x%base+'0');
        x/=base;
    }
    return result;
}


