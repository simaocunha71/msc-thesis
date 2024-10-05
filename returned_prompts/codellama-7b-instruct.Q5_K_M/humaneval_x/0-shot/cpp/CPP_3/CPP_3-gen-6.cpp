	//write your code here
	bool ret = false;
	int balance = 0;
	for (int i = 0; i < operations.size(); i++)
	{
		if (operations[i] < 0)
		{
			ret = true;
			break;
		}
		balance += operations[i];
		if (balance < 0)
		{
			ret = true;
			break;
		}
	}
	return ret;
}
int main() {
	vector<int> operations = { 1, 2, -4, 5 };
	bool ret = below_zero(operations);
	printf("%d", ret);


}


