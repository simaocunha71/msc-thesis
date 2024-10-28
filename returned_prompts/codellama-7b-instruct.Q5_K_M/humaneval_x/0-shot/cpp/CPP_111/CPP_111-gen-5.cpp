	map<char,int> mapa;
	int count = 0;
	int i;
	for(i=0;i<test.length();i++){
		if(test[i] != ' '){
			if(mapa.find(test[i]) == mapa.end()){
				mapa[test[i]] = 1;
			}else{
				mapa[test[i]] += 1;
			}
		}
	}
	return mapa;
}
int main(){
	string test1 = "a b c";
	string test2 = "a b b a";
	string test3 = "a b c a b";
	string test4 = "b b b b a";
	string test5 = "";
	map<char,int> mapa;
	mapa = histogram(test1);
	cout << mapa;
}
