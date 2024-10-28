float pi = 3.14159;
float x = (a*a) + (b*b) + (c*c);
float y = 2 * (a*b + b*c + c*a);
float z = x - y;
float x2 = sqrt(x);
float y2 = sqrt(y);
float z2 = sqrt(z);
if(x2 == y2 && y2 == z2){
if (c*c == z2)
return true;
}
return false;
}
/*
int main(){
float a = 3, b = 4, c = 5;
if (right_angle_triangle(a, b, c))
printf("True");
else
printf("False");
}
*/
