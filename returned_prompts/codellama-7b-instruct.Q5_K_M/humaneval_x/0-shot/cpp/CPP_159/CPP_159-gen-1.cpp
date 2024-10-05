	if(number>=need){
		return {number+remaining,0};
	}
	else if(number<need){
		return {number+remaining-need,need-number};
	}
}
int main(){
	int number;
	int need;
	int remaining;
	vector<int> result;
	scanf("%d",&number);
	scanf("%d",&need);
	scanf("%d",&remaining);
	result=eat(number,need,remaining);
	printf("%d %d",result[0],result[1]);
	return 0;
}
