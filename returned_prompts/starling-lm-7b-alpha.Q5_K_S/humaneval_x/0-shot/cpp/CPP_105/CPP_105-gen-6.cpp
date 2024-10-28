	if(arr.empty())
		return {};
	vector<int> tmp;
	for(int i=0;i<arr.size();i++)
		if(arr[i]>=1 && arr[i]<=9)
			tmp.push_back(arr[i]);
	sort(tmp.begin(),tmp.end());
	reverse(tmp.begin(),tmp.end());
	vector<string> ret;
	map<int,string> m;
	m[1] = "One";
	m[2] = "Two";
	m[3] = "Three";
	m[4] = "Four";
	m[5] = "Five";
	m[6] = "Six";
	m[7] = "Seven";
	m[8] = "Eight";
	m[9] = "Nine";
	for(int i=0;i<tmp.size();i++)
		ret.push_back(m[tmp[i]]);
	return ret;
}
int main(){
	vector<int> arr = {2,1,1,4,5,8,2,3};
	printf("%s\n",(by_length(arr)).data());
	return 0;
}

















































































































































































































