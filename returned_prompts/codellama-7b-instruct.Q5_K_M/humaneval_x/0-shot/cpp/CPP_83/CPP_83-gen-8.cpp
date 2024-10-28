	int count = 0;
	for(int i=0;i<10;i++){
		if(i==1)
			count+=10;
		else if(i==n-1)
			count+=10;
		else
			count+=9;
	}
	return count;
}

int main(){

B:
	int n;
	scanf("%d",&n);
	printf("%d\n",starts_one_ends(n));
	return 0;
}



