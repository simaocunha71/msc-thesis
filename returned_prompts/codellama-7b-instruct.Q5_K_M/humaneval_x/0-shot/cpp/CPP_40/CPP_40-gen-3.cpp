	for(int i=0;i<l.size();i++)
	{
		for(int j=i+1;j<l.size();j++)
		{
			for(int k=j+1;k<l.size();k++)
			{
				if(l[i]+l[j]+l[k]==0)
					return true;
			}
		}
	}
	return false;
}
int main()
{
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(7);
	
	if(triples_sum_to_zero(v))
		printf("true\n");
	else
		printf("false\n");
	
	return 0;
}
