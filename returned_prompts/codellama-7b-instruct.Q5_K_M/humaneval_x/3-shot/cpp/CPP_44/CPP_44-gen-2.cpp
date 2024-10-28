    string result;
    int digit;
    while (x>0){
        digit=x%base;
        result.insert(result.begin(),'0'+digit);
        x/=base;
    }
    return result;
}


