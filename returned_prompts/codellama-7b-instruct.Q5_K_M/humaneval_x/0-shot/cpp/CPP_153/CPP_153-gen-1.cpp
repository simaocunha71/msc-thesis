	int count = 0;
	int max = 0;
	string max_str;
	for(int i = 0; i<extensions.size(); i++){
		int cur = 0;
		for(int j = 0; j<extensions[i].length(); j++){
			if(isupper(extensions[i][j])){
				cur++;
			}
		}
		if(cur > max){
			max = cur;
			max_str = extensions[i];
		}
	}
	return class_name + "." + max_str;
}
