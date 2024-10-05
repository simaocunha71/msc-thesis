    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return distance(str.begin(), unique(str.begin(), str.end()));
}


