	/* I tried the below code but it doesn't work
	int sum=0;
	string key="2357BDE";
	sort(num.begin(),num.end());
	sort(key.begin(),key.end());
	for(int i=0;i<num.length();i++)
	{
		if(num[i]==key[i])
		{
			sum++;
		}
	}
	return sum;
	*/
B:
	/* I tried the below code but it doesn't work too
	int sum=0;
	sort(num.begin(),num.end());
	for(int i=0;i<num.length();i++)
	{
		if(num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7'||num[i]=='B'||num[i]=='D')
		{
			sum++;
		}
	}
	return sum;
	*/
C:
	/* I tried the below code but it doesn't work too
	int sum=0;
	for(int i=0;i<num.length();i++)
	{
		if(num[i]==2||num[i]==3||num[i]==5||num[i]==7||num[i]=='B'||num[i]=='D')
		{
			sum++;
		}
	}
	return sum;
	*/
}
int main()
{
	string num;
	printf("Enter a hexadecimal number:");
	cin>>num;
	int ans=hex_key(num);
	printf("Number of prime hexadecimal digits:%d\n",ans);
	return 0;
}

