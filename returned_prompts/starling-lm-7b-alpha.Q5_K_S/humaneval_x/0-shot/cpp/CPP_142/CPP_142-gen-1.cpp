	int sum = 0;
	for(int i = 0; i < lst.size(); i++){
		if(i%3 == 0){
			lst[i] = lst[i]*lst[i];
		}
		if(i%4 == 0 && i%3 != 0){
			lst[i] = lst[i]*lst[i]*lst[i];
		}
		sum+=lst[i];
	}
	return sum;
}




/*
"
This function will take a vector of integers. For all entries in the vector, the function shall square the integer entry if its index is a 
multiple of 3 and will cube the integer entry if its index is a