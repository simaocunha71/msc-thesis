	int cnt1=0;
	int cnt2=0;
	for(int i=0;i<lst1.size();i++)
	{
		for(int j=0;j<lst1[i].size();j++)
		{
			cnt1++;
		}
	}
	for(int i=0;i<lst2.size();i++)
	{
		for(int j=0;j<lst2[i].size();j++)
		{
			cnt2++;
		}
	}
	if(cnt2>cnt1)
	{
		goto A;
	}
	else
	{
		return lst1;
	}
}
int main()
{
	vector<string> lst1;
	vector<string> lst2;
	lst1.push_back("hi");
	lst1.push_back("admin");
	lst2.push_back("hI");
	lst2.push_back("Hi");
	total_match(lst1,lst2);
	return 0;
}

