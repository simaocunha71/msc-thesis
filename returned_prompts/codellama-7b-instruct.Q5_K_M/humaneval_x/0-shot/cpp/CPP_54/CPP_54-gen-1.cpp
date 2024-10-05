	if(s0.size()!=s1.size())
		return false;
	string s11=s1;
	sort(s0.begin(),s0.end());
	sort(s11.begin(),s11.end());
	int i=0;
	while(s0[i]==s11[i])
		i++;
	if(i==s0.size())
		return true;
	else
		return false;
}
int main(){
	string s0,s1;
	scanf("%s",&s0);
	scanf("%s",&s1);
	if(same_chars(s0,s1))
		printf("true");
	else
		printf("false");
	return 0;
}
