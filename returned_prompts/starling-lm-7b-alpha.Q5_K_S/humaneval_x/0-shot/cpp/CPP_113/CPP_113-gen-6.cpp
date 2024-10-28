	for(int i = 0; i < lst.size(); i++)
	{
		int count = 0;
		for(int j = 0; j < lst[i].size(); j++)
		{
			if(lst[i][j]%2!=0)
			{
				count++;
			}
		}
		string s = "the number of odd elements ";
		string str = "";
		for(int k = 0; k < lst[i].size(); k++)
		{
			str += lst[i][k];
		}
		s += to_string(count) + "n the str" + to_string(count) + "ng " + to_string(count) + "f the " + to_string(count) + "nput." + "\"";
		lst[i] = s;
	}
	return lst;
}
int main(){
	vector<string> v = {"1234567","3","11111111"};
	odd_count(v);
	for(int i = 0; i < v.size(); i++)
	{
		printf("%s\n",v[i].c_str());
	}
}

































































































































































































