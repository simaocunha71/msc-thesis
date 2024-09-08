    if(a==int(a)&&b==int(b)&&c==int(c)){
        if(a+b==c||a+c==b||b+c==a){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        goto A;
    }
}


int main(){
    bool a;
    a=any_int(5, 2, 7);
    printf("%d",a);
    a=any_int(3, 2, 2);
    printf("%d",a);
    a=any_int(3, -2, 1);
    printf("%d",a);
    a=any_int(3.6, -2.2, 2);
    printf("%d",a);
    return 0;
}

