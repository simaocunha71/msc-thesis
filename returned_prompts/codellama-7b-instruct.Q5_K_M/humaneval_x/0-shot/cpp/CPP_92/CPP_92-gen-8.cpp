if(a==b+c||b==a+c||c==a+b)
return true;
else
return false;
}
int main(){
    float a,b,c;
    scanf("%f",&a);
    scanf("%f",&b);
    scanf("%f",&c);
    if(any_int(a,b,c))
    printf("true\n");
    else
    printf("false\n");
    return 0;
}
