	/*
	* First step is to split the string into a vector of strings.
	* The string will look like this: "(()()) ((())) () ((())()())"
	* So we will split this string into {"(()())", " ((()))", " ()", " ((())()())"}
	*/
	vector<string> paren_vec(20); //The size of this vector can be increased if there are more than 20 groups.
	int i=0;
	while (paren_string.size()){
		paren_vec[i] = paren_string.substr(0, paren_string.find(" ")); //The substr function returns a substring of the first " " number of characters.
		i++;
		paren_string = paren_string.substr(paren_string.find(" ")+1); //The substr function returns a substring of the first " " number of characters.
	}
	
	/*
	* Now we have a vector of strings that represent the groups.
	* Now we will calculate the level of nesting of the parentheses.
	* We will use a vector to store the level of nesting for each group.
	*/
	vector<int> level_vec(20);
	for (int j=0; j<paren_vec.size(); j++){
		int level = 0; //The level of nesting starts from 0.
		for (int k=0; k<paren_vec[j].size(); k++){ //The size of the group.
			if (paren_vec[j][k] == '('){ //If the current character is an open parenthesis, we increase the level of nesting.
				level++;
			}
			else if (paren_vec[j][k] == ')'){ //If the current character is a close parenthesis, we decrease the level of nesting.
				level--;
			}
		}
		level_vec[j] = level;
	}
	return level_vec;
}






















