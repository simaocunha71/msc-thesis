	for(map<string, string>::iterator i = dict.begin(); i != dict.end(); i++)
	{
		if(i->first[0] >= 'A' && i->first[0] <= 'Z')
		{
			for(int j = 0; j < i->first.size(); j++)
			{
				if(i->first[j] >= 'a' && i->first[j] <= 'z')
				{
					return false;
				}
			}
		}
		else if(i->first[0] >= 'a' && i->first[0] <= 'z')
		{
			for(int j = 0; j < i->first.size(); j++)
			{
				if(i->first[j] >= 'A' && i->first[j] <= 'Z')
				{
					return false;
				}
			}
		}
	}
	return true;
}

int main()
{
	map<string, string> dict;
	dict["A"] = "APPLE";
	dict["a"] = "BANANA";
	printf("%d\n", check_dict_case(dict));
	dict.clear();
	dict["A"] = "APPLE";
	dict["b"] = "BANANA";
	printf("%d\n", check_dict_case(dict));
	dict.clear();
	dict["A"] = "APPLE";
	dict["B"] = "BANANA";
	printf("%d\n", check_dict_case(dict));
	dict.clear();
	dict["Name"] = "John";
	dict["Age"] = "36";
	dict["City"] = "Houston";
	printf("%d\n", check_dict_case(dict));
	dict.clear();
	dict["STATE"] = "NC";
	dict["ZIP"] = "12345";
	printf("%d\n",