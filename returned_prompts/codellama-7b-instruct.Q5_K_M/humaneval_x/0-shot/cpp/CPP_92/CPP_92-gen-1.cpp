
if(a==b+c || b==a+c || c==a+b)
	return true;
else
	return false;
}

int main(){
	float x,y,z;
	printf("Enter the values:\n");
	scanf("%f%f%f",&x,&y,&z);
	if(any_int(x,y,z))
		printf("True\n");
	else
		printf("False\n");
	return 0;
}
