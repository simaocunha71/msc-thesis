	if(n<p)
		return n;
	else{
		n=2*n;
		goto A;
	}
}
int main(){
	int a,b;
	scanf("%d%d",&a,&b);
	printf("%d\n",modp(a,b));
	return 0;
}

