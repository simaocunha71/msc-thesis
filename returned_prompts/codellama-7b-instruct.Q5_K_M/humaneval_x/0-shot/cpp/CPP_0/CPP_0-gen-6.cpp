	if (numbers.empty()){
		return false;
	}
	float min_dist = threshold;
	for (int i = 0; i < numbers.size() - 1; i++){
		for (int j = i + 1; j < numbers.size(); j++){
			if (fabs(numbers[i] - numbers[j]) < min_dist){
				return true;
			}
		}
	}
	return false;
}











