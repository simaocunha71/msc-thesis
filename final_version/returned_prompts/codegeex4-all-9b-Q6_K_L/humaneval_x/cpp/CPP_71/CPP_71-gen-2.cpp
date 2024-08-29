    if(a+b>c && a+c>b && b+c>a){
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }
    else{
        return -1;
    }
}
int main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    float result=triangle_area(a,b,c);
    if(result==-1){
        printf("Not a valid triangle\n");
    }
    else{
        printf("The area of the triangle is %f\n",result);
    }
    return 0;
}
