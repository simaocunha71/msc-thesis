    string result;
    for (char &c : s) {
        if(isupper(c))
            result += char(((c - 'A' + 2*2) % 26) + 'A');
        else
            result += char(((c - 'a' + 2*2) % 26) + 'a');
    }
    return result;
}


