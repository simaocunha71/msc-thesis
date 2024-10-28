	if(a%b==0)
		return b;
	a=a%b;
	goto A;
}
int main(){
	int a=3, b=5;
	int result=greatest_common_divisor(a, b);
	printf("%d\n", result);
}
