	if(l.size() == 0){
		return -1;
	}
	float max = l[0];
	for(int i = 1; i < l.size(); i++){
		if(max < l[i]){
			max = l[i];
		}
	}
	return max;
}

