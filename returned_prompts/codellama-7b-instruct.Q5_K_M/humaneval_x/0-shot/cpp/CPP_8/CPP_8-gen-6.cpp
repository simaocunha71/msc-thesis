	vector<int> res;
	if(numbers.size() == 0)
	{
		res.push_back(0);
		res.push_back(1);
		return res;
	}
	else
	{
		int sum = 0;
		int prod = 1;
		for(int i = 0; i < numbers.size(); i++)
		{
			sum += numbers[i];
			prod *= numbers[i];
		}
		res.push_back(sum);
		res.push_back(prod);
		return res;
	}
}

int main()
{
	vector<int> nums = {1, 2, 3, 4};
	vector<int> res = sum_product(nums);
	printf("%d, %d\n", res[0], res[1]);
}
