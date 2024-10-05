    return len(txt) > 0 && len(txt) < 2 && txt[len(txt)-1] == ' ' || len(txt) > 0 && len(txt) < 2 && txt[len(txt)-1] == '\n' ||  len(txt) > 0 && len(txt) < 2 && txt[len(txt)-1] == '\t' || len(txt) > 0 && txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || len(txt) > 0 && txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z'
}



