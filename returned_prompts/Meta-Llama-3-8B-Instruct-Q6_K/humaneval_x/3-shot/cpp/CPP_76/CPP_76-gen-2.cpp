    double y = pow(n, 1.0);
    while(x>=y){
        if(x==y){
            return true;
        }
        x /= n;
        y *= n;
    }
    return false;
}