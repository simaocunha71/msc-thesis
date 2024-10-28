	vector<int> res;
	if(n==0){
		return res;
	}
	bool prime[n+1];
	for(int i=0;i<=n;i++){
		prime[i]=true;
	}
	prime[0]=false;
	prime[1]=false;
	for(int i=2;i<=n;i++){
		if(prime[i]){
			for(int j=i+i;j<=n;j+=i){
				prime[j]=false;
			}
		}
	}
	for(int i=0;i<n;i++){
		if(prime[i]){
			res.push_back(i);
		}
	}
	return res;
}
int main(){
	vector<int> res=count_up_to(18);
	for(int i=0;i<res.size();i++){
		printf("%d ",res[i]);
	}
	printf("\n");
	return 0;
}

























































































































































































































































