	map<char,int> my_map;
	string test;
	int i=0;
	int count=0;
	char letter;
	while(i<test.length()){
		letter=test[i];
		if(letter==' '){
			i++;
			continue;
		}
		count++;
		if(my_map.find(letter)==my_map.end()){
			my_map.insert(pair<char,int>(letter,count));
		}
		i++;
	}
	return my_map;
}

int main()
{
	string test;
	getline(cin,test);
	map<char,int> my_map=histogram(test);
	map<char,int>::iterator it;
	for(it=my_map.begin();it!=my_map.end();it++){
		cout<<it->first<<":"<<it->second<<endl;
	}
	return 0;
}
