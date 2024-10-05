    if(a+b<c||a+c<b||b+c<a)
    {
        return -1;
    }
    else
    {
        float s=(a+b+c)/2;
        return sqrt(s*(s-a)*(s-b)*(s-c));
    }
}
int main(){
    float a,b,c;
    scanf("%f%f%f",&a,&b,&c);
    printf("%.2f",triangle_area(a,b,c));
}