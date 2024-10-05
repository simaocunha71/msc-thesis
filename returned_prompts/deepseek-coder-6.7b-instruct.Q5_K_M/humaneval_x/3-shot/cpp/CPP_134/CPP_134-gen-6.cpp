    if (txt.back() >= 'a' && txt.back() <= 'z' || txt.back() >= 'A' && txt.back() <= 'Z') {
        if (txt.length() == 1 || txt[txt.length()-2] == ' ')
            return true;
    }
    return false;
}


