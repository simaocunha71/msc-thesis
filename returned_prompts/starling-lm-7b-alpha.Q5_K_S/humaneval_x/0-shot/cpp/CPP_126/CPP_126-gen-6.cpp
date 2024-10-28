	vector<int>::iterator it,jt;
	it = lst.begin();
	jt = lst.begin();
	for(; it != lst.end(); it++, jt++){
		if(*it != *jt){
			return false;
		}
	}
	return true;
}
int main(){
	vector<int> lst = {1, 2, 3, 4, 5};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 3, 4, 5, 6};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 3, 4, 5, 6, 7};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 3, 4, 5, 6, 7, 7};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 2, 3, 4, 5, 6, 7};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 2, 2, 3, 4, 5, 6, 7};
	printf("res:%d\n", is_sorted(lst));
	lst = {1, 2, 3, 4, 5, 6, 7, 8};
	printf("res:%d\n", is_sorted(lst));
	return 0;
}


















































































































