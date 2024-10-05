
int modp(int n,int p){
	if(n==0) return 1;
	if(n%2==0) return (2*modp(n/2,p))%p;
	return (modp(n-1,p)*n)%p;
}
