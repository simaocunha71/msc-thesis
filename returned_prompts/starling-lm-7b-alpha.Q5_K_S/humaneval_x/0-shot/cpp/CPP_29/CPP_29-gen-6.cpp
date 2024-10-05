	vector<string> vec;
	for (int i=0;i<strings.size();i++) {
		if (strings[i].find(prefix)==0) {
			vec.push_back(strings[i]);
		}
	}
	return vec;
}


D:
/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_