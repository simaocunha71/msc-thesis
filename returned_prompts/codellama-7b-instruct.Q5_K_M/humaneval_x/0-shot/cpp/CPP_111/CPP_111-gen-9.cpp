	map<char,int> result;
	map<char,int>::iterator it;
	int count;
	char letter;
	string temp;
	temp=test;
	for(int i=0;i<temp.length();i++){
		letter=temp[i];
		count=1;
		for(int j=i+1;j<temp.length();j++){
			if(temp[i]==temp[j])
				count++;
		}
		result.insert(pair<char,int>(letter,count));
	}
	return result;
}
