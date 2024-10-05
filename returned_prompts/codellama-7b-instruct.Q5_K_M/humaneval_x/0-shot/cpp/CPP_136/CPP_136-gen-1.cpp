	int neg = 0;
	int pos = 0;
	for(int i = 0; i < lst.size(); ++i){
		if(lst[i] < 0){
			neg = lst[i];
			break;
		}
	}
	for(int j = 0; j < lst.size(); ++j){
		if(lst[j] > 0){
			pos = lst[j];
			break;
		}
	}
	if(neg != 0 && pos != 0){
		return {neg, pos};
	}
	else if(neg == 0 && pos == 0){
		return {0, 0};
	}
	else if(neg != 0 && pos == 0){
		return {neg, 0};
	}
	else{
		return {0, pos};
	}
}
