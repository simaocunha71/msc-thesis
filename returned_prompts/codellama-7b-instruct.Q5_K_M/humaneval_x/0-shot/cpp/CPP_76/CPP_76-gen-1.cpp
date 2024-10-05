	if(x==1)
		return true;
	if(x<1){
		return false;
	}
	if(x==n){
		return true;
	}
	for(int i=2;i<=sqrt(x);i++){
		if(x%i==0)
			return false;
	}
	return true;
}
int main(){
	int x,n;
	scanf("%d%d",&x,&n);
	printf("%d",is_simple_power(x,n));
	return 0;
}
