    if(txt.length()==0) return false;
    if(txt.length()>1 && txt[txt.length()-1]==' ' && txt.length()>2 && isalpha(txt[txt.length()-2])) return false;
    return isalpha(txt[txt.length()-1]);
} // end of function


