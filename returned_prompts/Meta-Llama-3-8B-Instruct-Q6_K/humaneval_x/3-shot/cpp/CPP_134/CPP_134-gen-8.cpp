    if(txt.length() == 0) return false;
    if(isalnum(txt.back())) {
        if(txt.find_last_of(" ") == string::npos || txt.find_last_of(" ") > txt.find_last_of(txt.back()))
            return true;
    }
    return false;
}


