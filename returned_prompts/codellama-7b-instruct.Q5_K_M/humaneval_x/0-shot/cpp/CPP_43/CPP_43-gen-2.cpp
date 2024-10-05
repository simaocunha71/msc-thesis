	for(int i=0;i<l.size();i++){
		for(int j=i+1;j<l.size();j++){
			if(l[i]+l[j]==0){
				return true;
			}
		}
	}
	return false;
}

int main(){
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	v.push_back(5);
	v.push_back(6);
	v.push_back(7);
	v.push_back(8);
	v.push_back(9);
	v.push_back(10);
	v.push_back(11);
	v.push_back(12);
	v.push_back(13);
	v.push_back(14);
	v.push_back(15);
	v.push_back(16);
	v.push_back(17);
	v.push_back(18);
	v.push_back(19);
	v.push_back(20);
	if(pairs_sum_to_zero(v)){
		printf("true\n");
	}
	else{
		printf("false\n");
	}
	return 0;
}