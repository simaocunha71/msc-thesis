	if(n==1) return vector<int>({1});
	for(int i=2;i*i<=n;i++){
		if(n%i==0){
			vector<int> v=factorize(n/i);
			v.push_back(i);
			return v;
		}
	}
	return vector<int>({n});
}


// 
// 
// int main(){
// 	vector<int> v=factorize(8);
// 	for(int i=0;i<v.size();i++) printf("%d ",v[i]);
// }
