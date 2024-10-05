    float d;
    if((a*a)==(b*b)+(c*c)){
        return true;
    }
    else if((b*b)==(c*c)+(a*a)){
        return true;
    }
    else if((c*c)==(b*b)+(a*a)){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    float a,b,c;
    printf("Enter the length of a side of the triangle\n");
    scanf("%f",&a);
    printf("Enter the length of another side of the triangle\n");
    scanf("%f",&b);
    printf("Enter the length of another side of the triangle\n");
    scanf("%f",&c);
    if(right_angle_triangle(a,b,c)){
        printf("The sides of the triangle make up a right angled triangle\n");
    }
    else{
        printf("The sides of the triangle don't make up a right angled triangle\n");
    }
    return 0;
}


















































































































































































































































