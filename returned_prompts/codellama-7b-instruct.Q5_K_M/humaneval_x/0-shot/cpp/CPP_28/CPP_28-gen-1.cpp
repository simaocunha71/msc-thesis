	return strings[0] + concatenate(strings[1:])

B:
	for(int i = 0; i < strings.size(); i++){
		if(i != strings.size() - 1){
			result += strings[i] + " ";
		}
		else{
			result += strings[i];
		}
	}
	return result;
}
