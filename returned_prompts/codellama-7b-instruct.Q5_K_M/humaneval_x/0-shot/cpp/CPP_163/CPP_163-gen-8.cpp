	if(a>b){
		return {};
	}
	vector<int> ans;
	for(int i=a;i<=b;i++){
		if(i%2==0){
			ans.push_back(i);
		}
	}
	return ans;
}

int main(){
	vector<int> a = generate_integers(10, 14);
	printf("[");
	for(int i=0;i<a.size();i++){
		printf("%d ", a[i]);
	}
	printf("]");
	return 0;
}
