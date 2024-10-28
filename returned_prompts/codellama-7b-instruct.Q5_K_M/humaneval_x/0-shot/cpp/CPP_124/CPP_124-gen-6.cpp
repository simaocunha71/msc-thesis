	int length = date.size();
	if(length == 0){
		return false;
	}
	if(date[length - 1] == '-'){
		goto A;
	}
	else{
		if(date[length - 3] == '-'){
			goto A;
		}
		else{
			if(date[length - 6] == '-'){
				goto A;
			}
			else{
				if(date[0] != '0'){
					goto A;
				}
				else{
					if(date[1] != '0'){
						goto A;
					}
					else{
						if(date[2] != '0'){
							goto A;
						}
						else{
							if(date[3] != '0'){
								goto A;
							}
							else{
								if(date[4] != '0'){
									goto A;
								}
								else{
									if(date[5] != '0'){
										goto A;
									}
									else{
										if(date[6] != '0'){
											goto A;
										}
										else{
											if(date[7] != '0'){
												goto A;
