	vector<string> ans;
	if(s.size()==0)return ans;
	string tmp;
	for(int i=0;i<s.size();i++)if(s[i]!=' ')tmp+=s[i];
	for(int i=0;i<ans.size();i++)if(tmp==ans[i])continue A;
	if(tmp.size()==n){
		ans.push_back(tmp);
		tmp.clear();
	}
	for(int i=0;i<s.size();i++)if(s[i]==' '){
		i+=tmp.size();
		for(int j=i;j<s.size();j++)if(s[j]==' '){
			if(tmp.size()!=n)ans.push_back(tmp);
			tmp.clear();
			for(int k=i;k<j;k++)tmp+=s[k];
			i=j;
		}
		if(tmp.size()!=n)ans.push_back(tmp);
		tmp.clear();
	}
	return ans;
}

int main(){
	printf("%s\n","Nowcoder");
	return 0;
}




*/





































































































































































































