	for(int i=0;i<l.size();i++){
		for(int j=0;j<l.size();j++){
			if(l[i]+l[j]==0){
				return true;
			}
		}
	}
	return false;
}

int main(){
	vector<int> l;
	l.push_back(1);
	l.push_back(3);
	l.push_back(5);
	l.push_back(0);
	//l.push_back(2);
	//l.push_back(4);
	//l.push_back(-5);
	//l.push_back(3);
	//l.push_back(5);
	//l.push_back(7);
	//l.push_back(1);
	//l.push_back(2);
	//l.push_back(3);
	//l.push_back(7);
	if(pairs_sum_to_zero(l))
		printf("true\n");
	else
		printf("false\n");
}
