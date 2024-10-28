    if(a==0)
        return true;
    if(a<0)
        a=-a;
    int b=pow(a,1.0/3.0);
    if(b*b*b==a)
        return true;
    return false;
}
int main(){
    int a=64;
    bool b=iscuber(a);
    printf("%d",b);
}
