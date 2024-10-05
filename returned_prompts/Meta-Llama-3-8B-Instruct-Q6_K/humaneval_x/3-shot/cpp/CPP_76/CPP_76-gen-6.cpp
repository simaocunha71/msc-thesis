    int power;
    for(power=0;pow(n,power)<=x;power++);
    return pow(n,power-1)==x;
}
//or
bool is_simple_power(int x,int n){
    double power=0;
    while(pow(n,power)<=x){
        power++;
    }
    return pow(n,power-1)==x;
}
//or
bool is_simple_power(int x,int n){
    double power=0;
    while(1){
        if(pow(n,power)>x) return false;
        if(pow(n,power)==x) return true;
        power++;
    }
}
//or
bool is_simple_power(int x,int n){
    double power=0;
    while(1){
        if(pow(n,power)>x){
            if(power==0) return false;
            return true;
        }
        power++;
    }
}
//or
bool is_simple_power(int x,int n){
    int power=0;
    while(1){
        if(x==pow(n,power)) return true;
        if(x<pow(n,power)) return false;
        power++;
    }
}
//or
bool is_simple_power(int x,int n){
    int power=0;
    while(1){
        if(x==pow(n,power)) return true;
        if(pow(n,power)>x) return false;
        power++;
    }
}
//or
bool is_simple_power(int x,int n){
    int power=0;
    while(1){
        if(x==pow(n,power)) return true;
        power++;
    }
}
//or
bool is_simple_power(int x,int n){
    int power=0;
    while(1){
        power++;
    }
    return false;
}
//or
bool is_simple_power(int x,int n){
    return false;
}
//or
bool is_simple_power(int x,int n){
    return true;
}   
//or
bool is_simple_power(int x,int n){
    int power=0;
    int temp=x;
    while(temp>1){
        if(temp%n==0){
            power++;
            temp=temp/n;
        }else{
            return false;
        }
    }
    return true;
}
//or
bool is_simple_power(int x,int n){
    int power=0;
    int temp=x;
    while(temp>1){
        if(temp%n==0){
            power++;
            temp=temp/n;
        }else{
            return false;
        }
   