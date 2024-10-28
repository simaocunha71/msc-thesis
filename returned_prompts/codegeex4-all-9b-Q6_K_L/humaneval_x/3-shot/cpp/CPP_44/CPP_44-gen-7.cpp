    string result;
    int div;
    while (x>0){
        div=x%base;
        result+=to_string(div);
        x=x/base;
    }
    reverse(result.begin(),result.end());
    return result;
}

