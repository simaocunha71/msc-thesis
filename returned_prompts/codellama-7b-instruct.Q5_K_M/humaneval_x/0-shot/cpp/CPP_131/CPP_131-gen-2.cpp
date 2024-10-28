	if(n==0) return 0;
	if(n%10==0){
		n/=10;
		goto A;
	}
	int a=0;
	while(n){
		if(n%10) a*=n%10;
		n/=10;
	}
	return a;
}
int main(){
	printf("%d",digits(235));
	return 0;
}
