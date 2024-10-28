
    if(a*a+b*b==c*c){
        return true;
    }
    else{
        return false;
    }

}

int main(){
    float a,b,c;
    printf("Enter the length of three sides of a triangle: ");
    scanf("%f %f %f", &a,&b,&c);
    printf("%d",right_angle_triangle(a,b,c));
}

