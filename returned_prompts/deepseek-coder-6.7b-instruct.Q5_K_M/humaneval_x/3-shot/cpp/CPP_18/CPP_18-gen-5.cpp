    int count = 0;
    size_t found = str.find(substring);
    while (found != std::string::npos){
        count++;
        found = str.find(substring, found+1);
    }
    return count;
}


