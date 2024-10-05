    if (txt.size()==0)
    return false;
    if (txt[txt.size()-1]>=65 && txt[txt.size()-1]<=90)
    return true;
    if (txt[txt.size()-1]>=97 && txt[txt.size()-1]<=122)
    return true;
    return false;
}


