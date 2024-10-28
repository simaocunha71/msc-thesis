    int a = stoi(s.substr(0,s.find(' ')));
    int o = stoi(s.substr(s.find_last_of(' ')+1));
    return n - a - o;
}


