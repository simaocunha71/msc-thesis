    int i = 1;
    while (i <= x){
        if(pow(n, i) == x){
            return true;
        }
        i++;
    }
    return false;
}


