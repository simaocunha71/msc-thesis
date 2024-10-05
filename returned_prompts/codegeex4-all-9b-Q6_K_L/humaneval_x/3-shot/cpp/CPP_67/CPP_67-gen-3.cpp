    int apples,oranges;
    apples=atoi(strtok((char*)s.c_str()," "));
    oranges=atoi(strtok(NULL," "));
    return n-apples-oranges;
}

