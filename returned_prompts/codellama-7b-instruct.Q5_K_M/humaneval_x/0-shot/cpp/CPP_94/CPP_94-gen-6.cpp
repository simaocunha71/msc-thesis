	vector<int> maxv;
	int max=0;
	int sum=0;
	for(int i=0;i<lst.size();i++){
		if(lst[i]>max){
			max=lst[i];
		}
	}
	for(int i=0;i<lst.size();i++){
		if(lst[i]==max){
			sum+=lst[i];
		}
	}
	return sum;
}
int main(){
	vector<int> lst;
	int n;
	cin>>n;
	while(n-->0){
		int t;
		cin>>t;
		lst.push_back(t);
	}
	int output=skjkasdkd(lst);
	cout<<output;
	return 0;
}

