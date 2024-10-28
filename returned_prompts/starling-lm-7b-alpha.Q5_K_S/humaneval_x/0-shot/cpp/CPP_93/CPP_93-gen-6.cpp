	int n = message.size();
	for(int i = 0; i < n; i++){
		if(message[i] >= 'a' && message[i] <= 'z'){
			message[i] += ('A' - 'a');
		}else if(message[i] >= 'A' && message[i] <= 'Z'){
			message[i] += ('a' - 'A');
		}
	}
	n = message.size();
	for(int i = 0; i < n; i++){
		if(message[i] == 'a') message[i] = 'c';
		else if(message[i] == 'e') message[i] = 'g';
		else if(message[i] == 'i') message[i] = 'k';
		else if(message[i] == 'o') message[i] = 'u';
		else if(message[i] == 'u') message[i] = 'i';
	}
	return message;
}

int main(){
	string message;
	getline(cin, message);
	printf("%s", encode(message).c_str());
}


/*
Test:
This is a message
tHKS KS C MGSSCGG
*/



/*
Test:
test
TGST
*/



/*
Test:
This is a message
tHKS KS C MGSSCGG
*/



/*
Test:
test
TGST
*/



/*
Test:
This is a message
tHKS KS C MGSSCGG
*/



/*
Test:
test
TGST
*/



/*
Test:
This is a message
tHKS KS C MGSSCGG
*/



/*
Test:
test
TGST
*/



/*
Test:
This is a message
tHKS KS C MGSSCGG
*/



/*
Test:
test
TGST
*/



/*
Test:
