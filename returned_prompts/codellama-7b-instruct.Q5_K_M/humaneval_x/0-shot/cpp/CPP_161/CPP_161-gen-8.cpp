	for(int i=0;i<s.size();i++)
	{
		if(s[i]>='a'&&s[i]<='z')
		{
			s[i]=toupper(s[i]);
			continue;
		}
		if(s[i]>='A'&&s[i]<='Z')
		{
			s[i]=tolower(s[i]);
			continue;
		}
	}
	return s;

}
