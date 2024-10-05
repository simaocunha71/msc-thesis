	int n = s.size();
	for(int i = 0; i < n; i++)
		if(s[i] >= 'a' && s[i] <= 'z')
			s[i] = 'A' + s[i] - 'a';
		else if(s[i] >= 'A' && s[i] <= 'Z')
			s[i] = 'a' + s[i] - 'A';
	return s;
}

int main()
{
	string s;
	while(cin >> s)
		printf("%s\n", solve(s).c_str());
	return 0;
}








```