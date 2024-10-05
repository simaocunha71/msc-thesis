	vector<string>temp;
	for(int i=0;i<words.size();i++){
		int j=0;
		for(j=0;j<words.size();j++){
			if(words[i]==words[j])
				break;
		}
		if(j==i){
			temp.push_back(words[i]);
		}
	}
	sort(temp.begin(),temp.end());
	return temp[temp.size()-1];
}
int main(){
	vector<string>words;
	string test1="abc";
	string test2="def";
	string test3="abcd";
	words.push_back(test1);
	words.push_back(test2);
	words.push_back(test3);
	string res=find_max(words);
	printf("%s\n",res.c_str());
	return 0;
}

