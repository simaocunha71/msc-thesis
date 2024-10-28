	if(a == 0) return b;
	if(b == 0) return a;
	goto A;
}
int main(){
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", greatest_common_divisor(a, b));
	