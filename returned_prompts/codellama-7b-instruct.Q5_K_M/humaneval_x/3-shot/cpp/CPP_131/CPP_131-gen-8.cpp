    string number=to_string(n);
    int result=1;
    for (int i=0;i<number.length();i++){
        if (number[i]-'0'%2==1)
        result*=number[i]-'0';
    }
    return result;
}



