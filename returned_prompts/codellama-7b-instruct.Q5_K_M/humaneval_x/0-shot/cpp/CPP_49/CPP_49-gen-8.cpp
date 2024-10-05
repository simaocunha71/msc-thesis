	return n%p;
}
int main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int n,p;
		scanf("%d%d",&n,&p);
		printf("%d\n",modp(n,p));
	}
}
