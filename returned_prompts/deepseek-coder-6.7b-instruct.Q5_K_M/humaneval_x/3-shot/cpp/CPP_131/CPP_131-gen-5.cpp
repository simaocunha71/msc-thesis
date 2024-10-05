    int product=1;
    string s = to_string(n);
    for(char c: s){
        int d = c - '0';
        if(d % 2 != 0)
            product *= d;
    }
    return product;
}


