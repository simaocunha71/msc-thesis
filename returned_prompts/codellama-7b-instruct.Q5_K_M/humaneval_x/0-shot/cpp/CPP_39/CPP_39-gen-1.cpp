	int a = 0, b = 1, c = a+b, flag = 0;
	while(n){
		c = a+b;
		if(is_prime(c) == 1)
			flag = 1;
		a = b;
		b = c;
		n--;
	}
	if(flag == 1)
		return c;
	else
		goto A;
}
int is_prime(int n){
	if(n == 1 || n == 0)
		return 0;
	else if(n == 2)
		return 1;
	else if(n%2 == 0)
		return 0;
	else{
		for(int i = 3; i*i <= n; i+=2)
			if(n%i == 0)
				return 0;
		return 1;
	}
}


int main(){
	int n;
	while(scanf("%d", &n) != EOF){
		if(n == 0)
			break;
		printf("%d\n", prime_fib(n));
	}
	return 0;
}
