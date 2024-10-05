	int odd_num=0;
	int even_num=0;
	int count=0;
	for(int i=0;i<arr.size();i++)
	{
		if(i<arr.size()/2)
		{
			if(arr[i]!=arr[arr.size()-i-1])
			{
				count++;
			}
		}
		else
		{
			if(arr[i]!=arr[arr.size()-i-1])
			{
				odd_num++;
			}
		}
	}
	int m;
	if(odd_num==0)
	{
		m=0;
	}
	else
	{
		m=odd_num/2+odd_num%2;
	}
	return count+m;
}
int main(void)
{
	vector<int> vec;
	int a;
	while(scanf("%d",&a)!=EOF)
	{
		vec.push_back(a);
	}
	printf("%d\n",smallest_change(vec));
	return 0;
}

*/
















































































































































































































