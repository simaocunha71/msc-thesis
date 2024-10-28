	for(int i=0;i<strings.size();i++){
		if(strings[i].find(substring) != string::npos)
			return strings;
		else
			return {};
	}
}
