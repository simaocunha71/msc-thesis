    if(a==b+c || b==a+c || c==a+b){
        return true;
    }
    else if(a==b || b==c || c==a){
        return false;
    }
    else{
        printf("The numbers are not integers\n");
        goto A;
    }
}
int main(){
    float a,b,c;
    printf("Enter the three numbers: ");
    scanf("%f%f%f",&a,&b,&c);
    if(any_int(a,b,c)==true){
        printf("The numbers are integers\n");
    }
    else{
        printf("The numbers are not integers\n");
    }
    return 0;
}
