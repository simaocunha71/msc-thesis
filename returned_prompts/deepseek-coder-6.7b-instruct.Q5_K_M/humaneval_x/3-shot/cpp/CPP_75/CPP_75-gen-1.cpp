    int count = 0;
    for(int i = 2; i <= a; ++i) {
        while(a % i == 0) {
            a /= i;
            ++count;
            if(count > 3) return false;
        }
    }
    return count == 3;
}

