    if (a<=0){
        return true;
    }
    if (a>0){
        for (int i=1;i<=a;i++){
            if (pow(i,3)==a){
                return true;
            }
        }
    }
    return false;
}



