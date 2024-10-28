	map<char,int> out;
	stringstream ss(test);
	string temp;
	while(getline(ss,temp,' ')){
		if(out.find(temp[0])==out.end()){
			out.insert(make_pair(temp[0],1));
		}else{
			out[temp[0]]++;
		}
	}
	return out;
}

