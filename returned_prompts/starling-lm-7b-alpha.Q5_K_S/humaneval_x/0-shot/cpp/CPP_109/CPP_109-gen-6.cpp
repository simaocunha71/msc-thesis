	for(int i=1;i<arr.size();i++)
	{
		if(arr[i]<arr[i-1])
		{
			for(int j=arr.size()-1;j>0;j--)
			{
				if(arr[j]>arr[j-1])
				{
					int tmp=arr[j];
					arr[j]=arr[j-1];
					arr[j-1]=tmp;
					goto A;
				}
			}
			return false;
		}
	}
	return true;
}
int main()
{
	vector<int> arr={3, 4, 5, 1, 2};
	if(move_one_ball(arr))
		printf("true\n");
	else
		printf("false\n");
	return 0;
}

*/










































































































































































































































































