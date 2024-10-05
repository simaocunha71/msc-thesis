	int num_len = num.length();
	int count = 0;
	for (int i = 0; i < num_len; i++) {
		if (num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7') {
			count++;
		}
		else if (num[i] == 'A' || num[i] == 'B' || num[i] == 'C' || num[i] == 'D' || num[i] == 'E' || num[i] == 'F') {
			if (num[i] == 'A') {
				if (i + 1 < num_len) {
					if (num[i + 1] == 'B') {
						count++;
					}
				}
			}
			else if (num[i] == 'B') {
				if (i + 1 < num_len) {
					if (num[i + 1] == 'D') {
						count++;
					}
				}
			}
			else if (num[i] == 'D') {
				if (i + 1 < num_len) {
					if (num[i + 1] == 'E') {
						count++;
					}
				}
			}
			else if (num[i] == 'E') {
				if (i + 1 < num_len) {
					if (num[i + 1] == 'F') {
						count++;
					}
				}
			}
		}
	}
	return count;
}
int main() {
	string num;
	cin >> num;
	printf("%d\n", hex_key(num));
