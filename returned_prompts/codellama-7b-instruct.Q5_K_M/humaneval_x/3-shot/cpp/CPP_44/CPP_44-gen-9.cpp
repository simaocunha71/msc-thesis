    string result="";
    while (x){
        result=char(x%base)+result;
        x=x/base;
    }
    return result;
}


