    int i;
    for (i=2;i<10;i++)
    if (a%i==0 && is_prime(i)){
        return true;
    }
    return false;
}


