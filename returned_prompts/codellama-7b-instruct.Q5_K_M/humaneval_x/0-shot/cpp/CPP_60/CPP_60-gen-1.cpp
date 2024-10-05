	if(n == 1)
		return 1;
	else if(n == 0)
		return 0;
	else
		return n + sum_to_n(n-1);
}

int main(){
	int input;
	while(1){
		scanf("%d",&input);
		if(input == 0)
			break;
		printf("%d\n",sum_to_n(input));
	}
	return 0;
}
