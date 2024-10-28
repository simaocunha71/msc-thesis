	int n = operato.size();
	int m = operand.size();
	int i, j;

	for(i = 0; i < n; ++i){
		if(operato[i] != "+"){
			if(operato[i] != "*"){
				if(operato[i] != "-"){
					if(operato[i] != "//"){
						if(operato[i] != "**"){
							printf("error\n");
							return -1;
						}
					}
				}
			}
		}
	}

	int t = 0;
	int ans = 0;
	for(i = 0; i < n; ++i){
		if(operato[i] == "+"){
			ans += operand[t];
			t++;
		}
		else if(operato[i] == "*"){
			ans *= operand[t];
			t++;
		}
		else if(operato[i] == "-"){
			ans -= operand[t];
			t++;
		}
		else if(operato[i] == "//"){
			ans = int(ans / operand[t]);
			t++;
		}
		else if(operato[i] == "**"){
			ans = int(pow(ans, operand[t]));
			t++;
		}
	}

	return ans;
}

int main(){
	int n;
	scanf("%d", &n);
	vector<string> operato(n);
	vector<int> operand(n);
	for(int i = 0; i < n; ++i)
		scanf("%s", &operato[i]);
	for(int i = 0; i < n; ++i)
		scanf("%d", &oper