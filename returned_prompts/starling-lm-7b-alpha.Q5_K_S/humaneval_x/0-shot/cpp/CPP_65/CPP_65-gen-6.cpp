	int digits,n;
	string s;
	digits = 0;
	n = x;
	while(n){
		n /= 10;
		digits++;
	}
	if(digits <= shift){
		s = "";
		while(digits--){
			s = char(x%10 + '0') + s;
			x /= 10;
		}
		return s;
	}
	s = "";
	while(digits--){
		s = char(x%10 + '0') + s;
		x /= 10;
	}
	for(int i=digits-shift;i<digits-1;i++)
		s = s.substr(0,i) + s.substr(i+1) + s.substr(i,1);
	return s;
}

int main(){
	int x,shift;
	scanf("%d%d",&x,&shift);
	printf("%s\n",circular_shift(x,shift).c_str());
}

















































































































































































































































