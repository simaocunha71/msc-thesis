    string s = to_string(n);
    int product=1, digit;
    for(int i=0; i<s.length(); i++){
        digit = s[i] - '0';
        if(digit % 2 != 0)
            product *= digit;
    }
    return (product==1) ? 0 : product;
}

