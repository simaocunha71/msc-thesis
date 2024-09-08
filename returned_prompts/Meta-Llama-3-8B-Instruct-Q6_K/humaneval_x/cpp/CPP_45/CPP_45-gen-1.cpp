float area;
area = (a*h)/2;
return area;
}
int main() {
   float a,h;
   printf("Enter side length: ");
   scanf("%f",&a);
   printf("Enter height: ");
   scanf("%f",&h);
   printf("Area of triangle: %.2f\n",triangle_area(a,h));
   return 0;
}

