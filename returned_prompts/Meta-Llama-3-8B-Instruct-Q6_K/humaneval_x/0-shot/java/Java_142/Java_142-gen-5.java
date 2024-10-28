    int sum = 0;
    for(int i = 0; i < lst.size(); i++) {
        if(i % 3 == 0 && i % 4 != 0) {
            sum += lst.get(i) * lst.get(i) * lst.get(i); // cube the integer entry
        } else if(i % 4 == 0 && i % 3 != 0) {
            sum += lst.get(i) * lst.get(i); // square the integer entry
        } else {
            sum += lst.get(i); // add the integer entry as it is
        }
    }
    return sum;
}