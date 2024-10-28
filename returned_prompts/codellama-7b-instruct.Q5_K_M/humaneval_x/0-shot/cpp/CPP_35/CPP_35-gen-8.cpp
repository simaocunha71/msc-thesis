	for(int i=0; i<l.size(); i++){
		for(int j=i+1; j<l.size(); j++){
			if(l[i]<l[j]){
				l[i] = l[j];
				goto A;
			}
		}
	}
	return l[0];
}
