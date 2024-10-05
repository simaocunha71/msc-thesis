	string ans;

	vector<pair<int,string>> v;
	v.push_back(make_pair(1000,"m"));
	v.push_back(make_pair(900,"cm"));
	v.push_back(make_pair(500,"d"));
	v.push_back(make_pair(400,"cd"));
	v.push_back(make_pair(100,"c"));
	v.push_back(make_pair(90,"xc"));
	v.push_back(make_pair(50,"l"));
	v.push_back(make_pair(40,"xl"));
	v.push_back(make_pair(10,"x"));
	v.push_back(make_pair(9,"ix"));
	v.push_back(make_pair(5,"v"));
	v.push_back(make_pair(4,"iv"));
	v.push_back(make_pair(1,"i"));

	while(number){
		for(auto &i:v){
			if(number>=i.first){
				ans+=i.second;
				number-=i.first;
				goto A;
			}
		}
	}
	return ans;
}








/*
Roman numerals are constructed by inscribing one of ten symbols in any order—though the order is almost always from left to right—above a line to represent a specific integer value. The numerals are:

I 1
X 10
C 100
D 500
M 1000

To represent an integer, one or more of these symbols is combined in a manner that expresses the desired value. For example, to represent the number 2018, one would write MMMDCCXVIII. In the centuries-long history of Roman civilization, Roman numerals have been used in various forms by many advanced civilizations, including the Byzantine Empire, the Islamic Golden Age, and the Sassanian Empire.

Here are some rules to follow when combining symbols:
