    if((a%1==0)&&(b%1==0)&&(c%1==0)){
        if((a==b+c)||(b==a+c)||(c==a+b)){
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
    float a,b,c;
    printf("Enter three numbers\n");
    scanf("%f%f%f",&a,&b,&c);
    printf("%d",any_int(a,b,c));
    return 0;
}
