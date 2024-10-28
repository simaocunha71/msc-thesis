    int apples=0;
    int oranges=0;
    stringstream ss(s);
    string sub;
    while(getline(ss, sub, ' '))
    {
        if (sub=="apples"){
            ss >> apples;
        }
        if (sub=="oranges"){
            ss >> oranges;
        }
    }
    return n-apples-oranges;
}


