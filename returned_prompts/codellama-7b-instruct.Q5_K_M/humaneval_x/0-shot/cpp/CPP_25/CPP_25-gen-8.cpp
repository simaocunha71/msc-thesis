	int i = 2;
	while(i < n){
		if(n % i == 0){
			n /= i;
			i = 2;
			continue;
		}
		i++;
	}
	if(i == n){
		i = 2;
		vector<int> ret;
		while(i < n){
			ret.push_back(n / i);
			i++;
		}
		return ret;
	}
	else
		goto A;
}
int main(){
	int n = 25;
	vector<int> ret = factorize(n);
	for(int i = 0; i < ret.size(); i++)
		printf("%d ", ret[i]);
	return 0;
}
