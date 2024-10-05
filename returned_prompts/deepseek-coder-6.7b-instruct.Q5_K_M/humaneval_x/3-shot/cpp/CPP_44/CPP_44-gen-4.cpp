    string result;
    int mod;
    while(x > 0){
        mod = x % base;
        result = to_string(mod) + result;
        x = x / base;
    }
    return result;
}


