	for(int i=0; i<num.size(); i++){
		if(num[i]=='0'||num[i]=='1'||num[i]=='2'||num[i]=='3'||num[i]=='4'||num[i]=='5'||num[i]=='6'||num[i]=='7'||num[i]=='8'||num[i]=='9'){
			if(num[i]=='0'||num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7'||num[i]=='9'){
				goto A;
			}else{
				return 0;
			}
		}else if(num[i]=='A'||num[i]=='B'||num[i]=='C'||num[i]=='D'||num[i]=='E'||num[i]=='F'){
			if(num[i]=='A'||num[i]=='C'||num[i]=='D'||num[i]=='E'||num[i]=='F'){
				return 0;
			}
		}
	}
return 1;
}
int main(){
	string num;
	int sum;
	scanf("%s",&num);
	if(hex_key(num)==0){
		printf("0");
	}else{
		sum=0;
		for(int i=0; i<num.size(); i++){
			if(num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7'||num[i]=='B'||num[i]=='D'||num[i]=='E'||num[i]=='F'){
				sum++;
			}
		}
		printf