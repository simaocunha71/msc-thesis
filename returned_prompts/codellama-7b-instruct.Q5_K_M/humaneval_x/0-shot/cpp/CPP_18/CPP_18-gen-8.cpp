    int count = 0;
    int pos = str.find(substring);
    if(pos == string::npos) return count;
    count++;
    str.erase(pos,substring.size());
    goto A;
}
