	vector<int> vec;
	for(int i=2;i<n;i++){
		bool isprime=true;
		for(int j=2;j<i;j++){
			if(i%j==0){
				isprime=false;
				break;
			}
		}
		if(isprime){
			vec.push_back(i);
		}
	}
	return vec;
}


