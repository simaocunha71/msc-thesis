	
	if (n==1) return 2;
	if (n==2) return 3;
	int a=5,b=8,c=13;
	for (int i=1;i<=n;i++){
		if (is_prime(c)){
			a=b;
			b=c;
			c=a+b;
		}
		else{
			c=b;
		}
	}
	return c;

}
bool is_prime(int n){
	if (n<2) return false;
	for (int i=2;i*i<=n;i++){
		if (n%i==0) return false;
	}
	return true;
}
int main(){
	int n=5;
	printf("%d",prime_fib(n));
	return 0;
}




















