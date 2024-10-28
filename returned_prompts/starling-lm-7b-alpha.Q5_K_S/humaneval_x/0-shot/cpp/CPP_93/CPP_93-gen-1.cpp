	for(int i = 0; i < message.length(); i++) {
		if((message[i] >= 'a' && message[i] <= 'z')||(message[i] >= 'A' && message[i] <= 'Z')) {
			if(message[i] == 'a' || message[i] == 'A') {
				message[i] = 'c';
			} else if(message[i] == 'b' || message[i] == 'B') {
				message[i] = 'd';
			} else if(message[i] == 'c' || message[i] == 'C') {
				message[i] = 'e';
			} else if(message[i] == 'd' || message[i] == 'D') {
				message[i] = 'f';
			} else if(message[i] == 'e' || message[i] == 'E') {
				message[i] = 'g';
			} else if(message[i] == 'f' || message[i] == 'F') {
				message[i] = 'h';
			} else if(message[i] == 'g' || message[i] == 'G') {
				message[i] = 'i';
			} else if(message[i] == 'h' || message[i] == 'H') {
				message[i] = 'j';
			} else if(message[i] == 'i' || message[i] == 'I') {
				message[i] = 'k';
			} else if(message[i] == 'j' || message[i] == 'J') {
				message[i] = 'l';
			} else if(message[i] == 'k' || message[i] == 'K') {
				message[i] = 'm';
			} else if(message[i] == 'l' || message[i] == 'L')