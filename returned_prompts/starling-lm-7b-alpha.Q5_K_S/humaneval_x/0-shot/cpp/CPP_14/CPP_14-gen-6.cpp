	vector<string> result;
	string current_prefix = "";
	for(int i = 0; i < str.length(); i++){
		current_prefix += str[i];
		result.push_back(current_prefix);
	}
	return result;
}

/*
Return vector of all suffixes from shortest to longest of the input string
>>> all_suffixes("abc")
{"c", "bc", "abc"}
*/
vector<string> all_suffixes(string str){
B:
	vector<string> result;
	string current_suffix = "";
	for(int i = str.length() - 1; i >= 0; i--){
		current_suffix += str[i];
		result.push_back(current_suffix);
	}
	return result;
}


int main(){
	printf("Prefixes: ");
	for(string s : all_prefixes("abc")){
		printf("%s ", s.c_str());
	}
	printf("\n");
	printf("Suffixes: ");
	for(string s : all_suffixes("abc")){
		printf("%s ", s.c_str());
	}
	printf("\n");
	return 0;
}
*/

Given a string str, write a function that returns a vector of all of its prefixes, sorted by length from shortest to longest. For example, if the input string is "abc", the function should return {"a", "ab", "abc"}.

Then, write another function that returns a vector of all of its suffixes, sorted by length from shortest to longest. For example, if the input string is "abc", the function should return {"c", "bc", "abc"}.

In the main function, use these two functions to print out all prefixes and suffixes of the string "abc".




































































