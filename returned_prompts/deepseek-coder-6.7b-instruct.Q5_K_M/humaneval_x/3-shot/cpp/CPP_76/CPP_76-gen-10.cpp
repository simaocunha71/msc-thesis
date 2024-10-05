    int power=0;
    while(pow(n,power)<=x){
        if(pow(n,power)==x)
        return true;
        power+=1;
    }
    return false;
}


