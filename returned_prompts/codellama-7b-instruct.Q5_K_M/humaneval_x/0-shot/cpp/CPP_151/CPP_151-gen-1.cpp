	if(lst.size()==0) return 0;
	long long sum=0;
	for(float i:lst){
		if(i<0 || (int)i!=i) goto A;
		sum+=pow(i, 2);
	}
	return sum;
}
