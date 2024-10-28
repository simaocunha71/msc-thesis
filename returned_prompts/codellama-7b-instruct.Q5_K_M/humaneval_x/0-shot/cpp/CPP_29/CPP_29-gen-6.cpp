	int len = 0;
	for (int i = 0; i < strings.size(); i++)
	{
		if (strings[i].compare(0, prefix.length(), prefix) == 0)
			len++;
	}
	vector<string> result;
	result.reserve(len);
	for (int i = 0; i < strings.size(); i++)
	{
		if (strings[i].compare(0, prefix.length(), prefix) == 0)
			result.push_back(strings[i]);
	}
	return result;
}
