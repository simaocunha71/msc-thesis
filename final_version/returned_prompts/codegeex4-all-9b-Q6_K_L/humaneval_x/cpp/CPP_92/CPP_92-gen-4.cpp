    if(a<=0||b<=0||c<=0){
        return false;
    }
    else if(a+b==c||a+c==b||b+c==a){
        return true;
    }
    else{
        goto A;
    }
}
int main(){
    float a,b,c;
    printf("Enter the three number\n");
    scanf("%f%f%f",&a,&b,&c);
    bool result=any_int(a,b,c);
    if(result==true){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}
B:
    if(a<=0||b<=0||c<=0){
        return false;
    }
    else if(a+b==c||a+c==b||b+c==a){
        return true;
    }
    else{
        goto B;
    }
}
int main(){
    float a,b,c;
    printf("Enter the three number\n");
    scanf("%f%f%f",&a,&b,&c);
    bool result=any_int(a,b,c);
    if(result==true){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}
C:
    if(a<=0||b<=0||c<=0){
        return false;
    }
    else if(a+b==c||a+c==b||b+c==a){
        return true;
    }
    else{
        goto C;
    }
}
int main(){
    float a,b,c;
    printf("Enter the three number\n");
    scanf("%f%f%f",&a,&b,&c);
    bool result=any_int(a,b,c);
    if(result==true){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}帮我检查一下代码

你的代码逻辑