	int len = lst.size();
	int i = 0;
	while(i < len){
		if(lst[i].size() % 2 == 1){
			lst.erase(lst.begin() + i);
			len--;
		}
		else i++;
	}

	sort(lst.begin(), lst.end());

	return lst;
}

int main(){
	vector<string> lst = {"aa", "a", "aaa"};
	vector<string> lst2 = {"ab", "a", "aaa", "cd"};

	vector<string> ans = sorted_list_sum(lst);

	for(int i = 0; i < ans.size(); i++){
		printf("%s ", ans[i].c_str());
	}
	printf("\n");
	ans = sorted_list_sum(lst2);

	for(int i = 0; i < ans.size(); i++){
		printf("%s ", ans[i].c_str());
	}
	printf("\n");

	return 0;
}













































































































































































































































