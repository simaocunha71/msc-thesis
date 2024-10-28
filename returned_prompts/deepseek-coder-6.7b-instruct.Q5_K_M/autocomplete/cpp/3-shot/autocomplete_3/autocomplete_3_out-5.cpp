	for  (int i 1; i 9; i++) {
		if (TL[map_key[i]] > TL[map_key[i+1]]) {
			tmp = map_key[i];
			map_key[i] = map_key[i+1];
			map_key[i+1] = tmp;
			i=0;
		}
	}

