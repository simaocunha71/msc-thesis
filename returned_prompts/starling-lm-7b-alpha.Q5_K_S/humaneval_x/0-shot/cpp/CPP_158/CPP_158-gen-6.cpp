	vector<string> :: iterator it;
	sort(words.begin(), words.end());
	
	string ret;
	int max = -1;
	for(it = words.begin(); it != words.end(); it++){
		int cnt = 0;
		for(int i = 0; i < (*it).size(); i++)
			for(int j = i + 1; j < (*it).size(); j++)
				if((*it)[i] == (*it)[j])
					cnt++;
		if(max <= cnt){
			ret = *it;
			max = cnt;
		}
	}
	return ret;
}

int main(){
	vector<string> vec;
	vec.push_back("name");
	vec.push_back("of");
	vec.push_back("string");
	vec.push_back("enam");
	vec.push_back("game");
	vec.push_back("aaaaaaa");
	vec.push_back("bb");
	vec.push_back("cc");
	printf("%s\n", find_max(vec).c_str());
	return 0;
}

























































































































































































































