    if(txt.length()==0 || isdigit(txt[txt.length()-1])) return false;
    if(txt.length()==1) return isalpha(txt[0]);
    return !isalpha(txt[txt.length()-1]) && (txt[txt.length()-2]==' ' || ispunct(txt[txt.length()-2]));
}



