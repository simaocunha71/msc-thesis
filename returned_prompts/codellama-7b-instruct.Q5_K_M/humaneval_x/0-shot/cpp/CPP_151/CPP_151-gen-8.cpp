	for(int i=0;i<lst.size();i++){
		if(lst[i]<0){
			lst.erase(lst.begin()+i);
			i--;
			goto A;
		}
		else if(lst[i]%2!=0){
			lst.erase(lst.begin()+i);
			i--;
			goto A;
		}
	}
	return 0;
}
