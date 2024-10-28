    int sum = 0;
    for(auto& c : s) {
        if(isupper(c)) sum += (int) c;
    }
    return sum;
}


