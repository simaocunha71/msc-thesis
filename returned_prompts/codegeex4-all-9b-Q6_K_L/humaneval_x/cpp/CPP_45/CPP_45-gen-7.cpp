    if(a<=0){
        printf("Invalid side\n");
        goto A;
    }
    else if(h<=0){
        printf("Invalid height\n");
        goto A;
    }
    else{
        return(a*h)/2;
    }

}
int main(){
    float a,h;
    scanf("%f",&a);
    scanf("%f",&h);
    printf("%f\n",triangle_area(a,h));
    return 0;
}

