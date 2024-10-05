	int apples = 0;
	int oranges = 0;
	int mango = 0;
	int i = 0;
	while(i<s.length()){
		if(s[i] == 'a'){
			apples++;
			i++;
			if(s[i] == 'n' && s[i+1] == 'g'){
				i += 2;
				break;
			}
			continue;
		}
		if(s[i] == 'o'){
			oranges++;
			i++;
			if(s[i] == 'r' && s[i+1] == 'a'){
				i += 2;
				break;
			}
			continue;
		}
		i++;
	}
	mango = n - apples - oranges;
	return mango;
}

