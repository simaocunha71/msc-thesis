	for(int i=0;i<s.length();i++)
	{
		if(s[i] >= 'A' && s[i] <= 'Z')
		{
			s[i] = s[i]+2;
			if(s[i]> 'Z')
			{
				s[i] = s[i] - 26;
			}
		}
		else if(s[i] >= 'a' && s[i] <= 'z')
		{
			s[i] = s[i]+2;
			if(s[i]> 'z')
			{
				s[i] = s[i] - 26;
			}
		}
	}
	return s;
}
int main()
{
	string s;
	scanf("%s",&s);
	printf("%s\n",encrypt(s).c_str());
	return 0;
}



































































































































































































































































