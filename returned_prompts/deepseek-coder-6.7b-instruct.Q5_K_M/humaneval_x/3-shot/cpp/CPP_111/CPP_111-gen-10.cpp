    map<char,int> counter;
    int i;
    for(i=0; i<test.length(); i++){
        counter[test[i]]++;
    }
    return counter;
}

