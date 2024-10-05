	float area=0.5*a*h;
	return area;
}
int main(){
	float a,h,area;
	printf("Enter length of side and height of triangle : ");
	scanf("%f %f",&a,&h);
	area=triangle_area(a,h);
	printf("The area of triangle is %.2f\n",area);
	return 0;
}

A: 
	float area=0.5*a*h;
	return area;


