    if(txt.length()==0) return false;
    if(!isalpha(txt[txt.length()-1])) return false;
    if(txt.length()==1) return true;
    if(txt[txt.length()-2]==' ') return true;
    return false;
}


