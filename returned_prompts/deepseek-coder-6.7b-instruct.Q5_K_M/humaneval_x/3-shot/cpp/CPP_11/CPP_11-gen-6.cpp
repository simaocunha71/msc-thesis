    string res = "";
    int len = a.length();
    for(int i=0;i<len;i++){
        res += to_string((a[i] - '0') ^ (b[i] - '0'));
    }
    return res;
}

