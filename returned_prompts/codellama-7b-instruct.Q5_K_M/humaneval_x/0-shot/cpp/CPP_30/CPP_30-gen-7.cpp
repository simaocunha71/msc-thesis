	for(int i = 0; i < l.size(); i++){
		if(l[i] < 0)
			l.erase(l.begin() + i);
	}
	return l;
}

