    if (x==0){
        return "0";
    }
    else{
        string ans="";
        while (x>0){
            ans+=(x%base);
            x/=base;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
}


