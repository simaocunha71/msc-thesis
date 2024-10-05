    string ans;
    while (x>0){
        ans=(x%base)+ans;
        x/=base;
    }
    return ans;
}


