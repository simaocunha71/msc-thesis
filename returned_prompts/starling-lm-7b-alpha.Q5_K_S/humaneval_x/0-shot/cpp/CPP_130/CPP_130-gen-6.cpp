	if(n==1)
	{
		vector<int> v;
		v.push_back(3);
		return v;
	}
	else if(n==0)
	{
		vector<int> v;
		return v;
	}
	else
	{
		vector<int> v=tri(n/2);
		int s=1;
		if(n%2==0)
		{
			s+=n/2;
		}
		else
		{
			vector<int> v1=tri(n-1);
			vector<int> v2=tri(n-2);
			vector<int> v3=tri(n+1);
			s=v1[v1.size()-1]+v2[v2.size()-1]+v3[v3.size()-1];
		}
		v.push_back(s);
		goto A;
	}

}
int main(void)
{
	int n;
	scanf("%d",&n);
	vector<int> v=tri(n);
	for(int i=0;i<v.size();i++)
	{
		printf("%d ",v[i]);
	}
	return 0;
}



*/

















































































































































































