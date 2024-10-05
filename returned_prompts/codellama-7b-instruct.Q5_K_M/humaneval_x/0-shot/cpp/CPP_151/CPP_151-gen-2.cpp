	if(lst.size() == 0) return 0;
	int i = 0;
	for(i = 0; i < lst.size(); i++){
		if(lst[i] < 0 || lst[i] != (int)lst[i]){
			goto A;
		}
	}
	float sum = 0;
	for(i = 0; i < lst.size(); i++){
		if(lst[i] % 2 != 0) sum += pow(lst[i], 2);
	}
	return sum;
}
