    if(b.length()==0) return false;
    if(a.find(b)!=string::npos) return true;
    else{
        for(int i=0;i<b.length();i++){
            char temp = b[i];
            b[i] = b[b.length()-i-1];
            b[b.length()-i-1] = temp;
        }
        goto A;
    }
    return false;
}


