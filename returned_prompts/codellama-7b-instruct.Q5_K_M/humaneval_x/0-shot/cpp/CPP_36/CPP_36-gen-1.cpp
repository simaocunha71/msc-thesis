	int cnt = 0;
	for(int i = 11; i < n; i++)
		if(i % 11 == 0 || i % 13 == 0){
			if(i % 7 == 0)
				cnt++;
		}
	return cnt;
}
