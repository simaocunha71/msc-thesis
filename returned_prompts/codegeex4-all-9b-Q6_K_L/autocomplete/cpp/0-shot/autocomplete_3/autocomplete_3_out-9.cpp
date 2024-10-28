	
	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			if (map_key[i] == TL[j]) {
				key[i] = key[i] + to_string(j);
			}
		}
	}
	
	for (int i = 0; i < len; i++) {
		for (int j = 1; j <= 9; j++) {
			if (key[TL[j]].find(s[i]) != string::npos) {
				cout << j;
				break;
			}
		}
	}

```cpp
	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			if (map_key[i] == TL[j]) {
				key[i] = key[i] + to_string(j);
			}
		}
	}

	for (int i = 0; i < len; i++) {
		for (int j = 1; j <= 9; j++) {
			if (key[TL[j]].find(s[i]) != string::npos) {
				cout << j;
				break;
			}
		}
	}
```
