    if(a==0||b==0||c==0){
        goto B;
    }
    if(a<=0||b<=0||c<=0){
        goto B;
    }
    if(a>=b+c||b>=a+c||c>=a+b){
        goto B;
    }
    if(a+b==c||b+c==a||a+c==b){
        goto A1;
    }
    if(a==b+c||b==a+c||c==a+b){
        goto A1;
    }
    if(a+b+c==0){
        goto A1;
    }
    return false;
B:
    if(a+b+c==0){
        goto A1;
    }
    if(a==b==c){
        goto A1;
    }
    if(a==0&&b==c){
        goto A1;
    }
    if(b==0&&a==c){
        goto A1;
    }
    if(c==0&&b==a){
        goto A1;
    }
    if(a==b||a==c||b==c){
        goto A1;
    }
    return false;
A