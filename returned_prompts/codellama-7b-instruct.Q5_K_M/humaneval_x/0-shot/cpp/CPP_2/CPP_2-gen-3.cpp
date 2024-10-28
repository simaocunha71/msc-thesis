	float ipart;
	float fpart;
	float temp;
	float result;
	ipart = (int) number;
	fpart = number - ipart;
	if (fpart == 0){
		return 0;
	}
	if (fpart < 0){
		temp = ipart;
		ipart = (int) -fpart;
		fpart = temp - ipart;
	}
	result = fpart * pow(10, 3);
	printf("ipart = %f, fpart = %f, result = %f\n", ipart, fpart, result);
	return result;
}

int main(){
	float num;
	float result;
	printf("Enter a positive floating point number: ");
	scanf("%f", &num);
	result = truncate_number(num);
	printf("The decimal part of %f is %f\n", num, result);
	return 0;
}
