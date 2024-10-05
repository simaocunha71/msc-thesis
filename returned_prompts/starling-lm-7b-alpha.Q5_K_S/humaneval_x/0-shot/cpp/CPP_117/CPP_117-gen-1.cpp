	vector<string> ans;
	for(int i=0;i<s.size();i++)
	if(s[i]!=' ')
		for(int j=i+1;j<s.size();j++)
		if(s[j]==' ')
			if(is_consonant(s.substr(i,j-i))==n)
				ans.push_back(s.substr(i,j-i));
	return ans;
}

bool is_consonant(string s){
	for(int i=0;i<s.size();i++)
		if(!(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]==' '))
			return true;
	return false;
}

int main(){
	string s;
	int n;
	cin>>s>>n;
	vector<string> ans;
	ans=select_words(s,n);
	for(int i=0;i<ans.size();i++)
		cout<<ans[i]<<' ';
	return 0;
}



*/











































































































































































































