	if(str.empty())
		return 0;
	if(substring.empty())
		return 0;
	if(str.size() < substring.size())
		return 0;
	if(str == substring)
		return 1;
	int i = str.find(substring);
	if(i == string::npos)
		return 0;
	str.replace(i,substring.size(),"");
	goto A;
}

int main(){
	string str;
	string sub;
	cout<<"Enter the string: ";
	cin>>str;
	cout<<"Enter the substring: ";
	cin>>sub;
	int x = how_many_times(str,sub);
	cout<<"The substring appears "<<x<<" times.";
	return 0;
}
