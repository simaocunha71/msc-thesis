    if(a > b && a > c){
        return pow(a, 2) == pow(b, 2) + pow(c, 2);
    }
    else if(b > a && b > c){
        return pow(b, 2) == pow(a, 2) + pow(c, 2);
    }
    else{
        return pow(c, 2) == pow(a, 2) + pow(b, 2);
    }
}


