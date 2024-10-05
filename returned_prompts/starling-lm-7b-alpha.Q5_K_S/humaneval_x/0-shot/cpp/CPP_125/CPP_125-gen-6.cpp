	if (txt.find(' ') != string::npos) {
		vector<string> res;
		int i = 0;
		while (i < txt.size()) {
			if (txt[i] == ' ') {
				res.push_back(txt.substr(0, i));
				txt = txt.substr(i + 1);
			}
			else
				i++;
		}
		res.push_back(txt);
		return res;
	}
	else if (txt.find(',') != string::npos) {
		vector<string> res;
		int i = 0;
		while (i < txt.size()) {
			if (txt[i] == ',') {
				res.push_back(txt.substr(0, i));
				txt = txt.substr(i + 1);
			}
			else
				i++;
		}
		res.push_back(txt);
		return res;
	}
	else {
		int count = 0;
		for (int i = 0;i<txt.size();i++)
			if ((txt[i] - 'a') % 2 == 1)
				count++;
		vector<string> res;
		res.push_back(to_string(count));
		return res;
	}
}

int main()
{
	string txt = "abcdef";
	vector<string> res = split_words(txt);
	for (int i = 0;i<res.size();i++)
		printf("%s ", res[i].c_str());
	printf("\n");
	return 0;
}





















*/











































