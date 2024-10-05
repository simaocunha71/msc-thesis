	float integer_part;
	float decimals;
	integer_part = (int)number;
	decimals = number - integer_part;
	if(decimals >= 1){
		goto A;
	}
	return decimals;
}
int main(){
	printf("0.5 = %f", truncate_number(3.5));
}
