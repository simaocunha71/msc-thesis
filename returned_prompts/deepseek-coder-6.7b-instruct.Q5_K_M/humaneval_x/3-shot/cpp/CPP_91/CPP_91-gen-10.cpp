    int count = 0;
    size_t found;
    while ((found = S.find_first_of(".?!")) != string::npos) {
        string sentence = S.substr(0, found+1);
        if (sentence[0] == 'I') {
            count++;
        }
        S = S.substr(found+1);
    }
    return count;
}

