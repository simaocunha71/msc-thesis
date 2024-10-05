    string result="";
    int a;
    while (x!=0){
        a=x%base;
        if (a>=0 && a<=9)
        result=a+result;
        else
        result=(a-10)+result;
        x=x/base;
    }
    return result;
}




