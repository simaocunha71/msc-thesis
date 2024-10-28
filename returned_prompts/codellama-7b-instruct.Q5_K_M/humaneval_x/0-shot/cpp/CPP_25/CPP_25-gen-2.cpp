	if(n==1)
		return vector<int>();
	for(int i=2;i<n;i++){
		if(n%i==0){
			vector<int> res=factorize(i);
			res.push_back(i);
			return res;
		}
	}
	return vector<int>();
}

// int main()
// {
// 	int n=0;
// 	scanf("%d",&n);
// 	vector<int> v=factorize(n);
// 	for(int i=0;i<v.size();i++){
// 		printf("%d ",v[i]);
// 	}
// 	return 0;
// }
