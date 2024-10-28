	if(dict.empty()) return false;
	bool lower = true;
	bool upper = true;

	for(auto it = dict.begin();it!=dict.end();it++){
		if(!it->first.empty() && it->first[0] >= 'A' && it->first[0] <= 'Z'){
			lower = false;
		}
		if(!it->first.empty() && it->first[0] >= 'a' && it->first[0] <= 'z'){
			upper = false;
		}
		if(lower == false && upper == false) goto A;
	}
	if(lower == true) return true;
	if(upper == true) return true;
	return false;
}

int main(){

	map<string,string> dict;
	dict.insert(pair<string,string>("a","apple"));
	dict.insert(pair<string,string>("b","banana"));
	if(check_dict_case(dict))
		printf("true\n");
	else
		printf("false\n");
	return 0;
}
