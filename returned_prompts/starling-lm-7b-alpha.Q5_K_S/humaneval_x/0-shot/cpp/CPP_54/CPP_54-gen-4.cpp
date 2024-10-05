	int a,b,i,j,c0,c1,flag;
	a=s0.length();
	b=s1.length();
	c0=0;
	c1=0;
	char s[a+b],t[a+b];
	for(i=0;i<a;i++){
		s[c0]=s0[i];
		c0++;
	}
	for(i=0;i<b;i++){
		t[c1]=s1[i];
		c1++;
	}
	sort(s,s+a+b);
	sort(t,t+a+b);
	for(i=0;i<a+b;i++){
		if(s[i]!=t[i]){
			flag=1;
			goto B;
		}
	}
	goto A;
B:
	return false;
}

int main()
{
	string s0,s1;
	while(cin>>s0>>s1){
		if(same_chars(s0,s1)) printf("true\n");
		else printf("false\n");
	}
	return 0;
}




















































































































































































































