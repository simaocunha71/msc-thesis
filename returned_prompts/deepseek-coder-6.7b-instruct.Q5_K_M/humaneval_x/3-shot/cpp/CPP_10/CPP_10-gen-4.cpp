    if(is_palindrome(str)){
        return str;
    }
    else{
        string rev(str.rbegin(), str.rend());
        string bstr = str + "#" + rev;
        int lps[bstr.length()];
        lps[0]=0;
        int i=1;
        int len=0;
        while(i<bstr.length()){
            if(bstr[i]==bstr[len]){
                len++;
                lps[i]=len;
                i++;
            }
            else{
                if(len==0){
                    lps[i]=0;
                    i++;
                }
                else{
                    len=lps[len-1];
                }
            }
        }
        int palin_len=lps[bstr.length()-1];
        string add=rev.substr(palin_len);
        return str+add;
    }
}

