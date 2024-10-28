	for (int i=0;i<n.size();i++){
		int sum=0;
		while(n[i]!=0){
			sum=sum+n[i]%10;
			n[i]=n[i]/10;
		}
		if(sum>0)
			return sum;
		else
			return 0;
	}
	return 0;
}
int main(){
	vector<int> n;
	n.push_back(-12);
	n.push_back(-13);
	n.push_back(-14);
	n.push_back(15);
	n.push_back(16);
	n.push_back(17);
	n.push_back(18);
	n.push_back(19);
	printf("%d",count_nums(n));
}

