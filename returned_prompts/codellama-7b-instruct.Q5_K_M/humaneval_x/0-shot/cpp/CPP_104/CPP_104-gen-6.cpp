	for (int i=0;i<x.size();i++){
		if (x[i]%2==0){
			x.erase(x.begin()+i);
			i--;
		}
	}
	sort(x.begin(),x.end());
	return x;
}

