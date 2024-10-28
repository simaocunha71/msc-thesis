	if (text.find_first_of("aeiouAEIOU")==string::npos) {
		return text;
	}
	text.erase(text.find_first_of("aeiouAEIOU"));
	goto A;
}

int main(){
	string test;
	while(cin>>test){
		printf("\"%s\"\n",remove_vowels(test).c_str());
	}
	return 0;
}
