    int i,product=1,remainder;
    string number_str=to_string(n);
    int len=number_str.length();
    for (i=0;i<len;i++)
    {
        remainder=number_str[i]-'0';
        if (remainder%2!=0){
        product*=remainder;
        }
    }
    return product;
}


