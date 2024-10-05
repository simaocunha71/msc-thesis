	int c0 = 0,c1 = 0;
	while(c0 < s0.length() && c1 < s1.length()){
		if(s0[c0] != s1[c1]){
			return false;
		}
		c0++;
		c1++;
	}
	if(c0 != s0.length() || c1 != s1.length()){
		return false;
	}
	return true;
}
int main(){
	string s0,s1;
	while(cin >> s0 >> s1){
		bool res = same_chars(s0,s1);
		printf("%d\n",res);
	}
}












































































































