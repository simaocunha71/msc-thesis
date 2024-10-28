	if(n<=1)
		return n;
	else{
		int a=fib4(n-1);
		int b=fib4(n-2);
		int c=fib4(n-3);
		int d=fib4(n-4);
		return a+b+c+d;
	}
}
int main(){
	printf("%d\n",fib4(5));
	printf("%d\n",fib4(6));
	printf("%d\n",fib4(7));
}
