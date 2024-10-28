	for(int i=0;i<l.size();i++){
		for(int j=i+1;j<l.size();j++){
			if(l[i]+l[j]==0)
				return true;
		}
	}
	return false;
}
int main(){
	vector<int> v{1,2,3,4,5};
	printf("result: %d",pairs_sum_to_zero(v));
	return 0;
}
