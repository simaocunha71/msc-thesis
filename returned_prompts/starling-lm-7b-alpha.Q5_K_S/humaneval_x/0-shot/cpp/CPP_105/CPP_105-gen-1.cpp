	sort(arr.begin(),arr.end());
	reverse(arr.begin(),arr.end());
	vector<string> res;
	map<int,string> mp = {
		{1,"One"},
		{2,"Two"},
		{3,"Three"},
		{4,"Four"},
		{5,"Five"},
		{6,"Six"},
		{7,"Seven"},
		{8,"Eight"},
		{9,"Nine"},
	};
	for(auto i : arr){
		if(i > 0 && i < 10){
			res.push_back(mp[i]);
		}
	}
	return res;
}

int main(){
	vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
	vector<string> res = by_length(arr);
	for(auto i : res){
		printf("%s ", i.c_str());
	}
	return 0;
}


*/























































































































































































































































