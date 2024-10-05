    for (int i = 0; i < b.length(); i++) {
        string rotated = b.substr(i) + b.substr(0, i);
        if (a.find(rotated) != string::npos) {
            return true;
        }
    }
    return false;
}


