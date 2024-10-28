    string str = to_string(x);
    int len = str.size();
    if(shift>=len){
        reverse(str.begin(), str.end());
        return str;
    }
    rotate(str.begin(),str.begin()+len-shift,str.end());
    return str;
}


