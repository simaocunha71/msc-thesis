    if(a<=0||h<=0){
        printf("a or h must be greater than 0\n");
        goto A;
    }
    else{
        float s=(a*h)/2;
        return s;
    }
}
int main(){
    float a,h;
    printf("enter the side and high of triangle\n");
    scanf("%f %f",&a,&h);
    float s=triangle_area(a,h);
    printf("area of triangle is=%f",s);
    return 0;
}
