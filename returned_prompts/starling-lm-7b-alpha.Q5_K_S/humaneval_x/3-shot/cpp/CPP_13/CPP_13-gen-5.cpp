    if (a==0){
        return b;
    }
    if (b==0){
        return a;
    }
    if (a==b){
        return a;
    }
    if (a>b){
        return greatest_common_divisor(a-b, b);
    }
    if (b>a){
        return greatest_common_divisor(b-a, a);
    }
}


