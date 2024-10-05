	map<char,int> m;

	for(int i=0;i<test.size();i++){
		m[test[i]]++;
	}
	map<char,int>::iterator it = m.begin();
	int max = 0;
	char ch;
	while(it!=m.end()){
		if(max < it->second){
			ch = it->first;
			max = it->second;
		}
		it++;
	}
	if(max == 1){
		m.erase(ch);
	}else if(m.size() == 2){
		m.erase(ch);
	}else if(m.size() > 2){
		it = m.begin();
		while(it!=m.end()){
			if(it->second == max){
				if(it != m.begin()){
					it--;
				}
				m.erase(it);
				break;
			}
			it++;
		}
	}
	return m;
}

int main(void){
	string test;
	while(cin >> test){
		map<char,int> ret = histogram(test);
		printf("{");
		map<char,int>::iterator it = ret.begin();
		while(it!=ret.end()){
			if(it != ret.begin()){
				printf(", ");
			}
			printf("{%c, %d}",it->first,it->second);
			it++;
		}
		printf("}\n");
	}
	return 0;
}

*/
















































































