
string str = "()";
string str1 = "()";
string str2 = "()";

vector<string> v;

v.push_back(str);
v.push_back(str1);
v.push_back(str2);

for(int i=0; i<v.size(); i++){

	for(int j=0; j<v.size(); j++){

		if(v.size()==1)
			return "Yes";
		
		if(v[i]==v[j]){
			v.erase(v.begin()+j);
			v.erase(v.begin()+i);
			goto A;
		}
	}
}

if(v.size()==1)
	return "Yes";
else
	return "No";
}
