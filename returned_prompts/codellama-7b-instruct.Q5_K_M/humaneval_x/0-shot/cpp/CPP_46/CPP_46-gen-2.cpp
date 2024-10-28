	if(n==0) return 0;
	if(n==1) return 0;
	if(n==2) return 2;
	if(n==3) return 0;
	if(n==4) return 0;
	else return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4);
}
int main(){
	int i;
	for(i=0;i<10;i++){
		printf("%d\n",fib4(i));
	}
}
