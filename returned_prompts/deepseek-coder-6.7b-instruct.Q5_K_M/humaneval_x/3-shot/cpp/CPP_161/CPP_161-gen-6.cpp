    string res="";
    for (auto c:s){
        if (isalpha(c)) res+=islower(c)?toupper(c):tolower(c);
        else res=c+res;
    }
    return res==""?s:res;
}


