	if(a+b>c && a+c>b && b+c>a)
		return sqrt(a*a+b*b+c*c);
	else
		return -1;
}
int main()
{
	float a,b,c;
	scanf("%f%f%f",&a,&b,&c);
	printf("%.2f",triangle_area(a,b,c));
	return 0;
}

