	int size = l.size();
	sort(l.begin(), l.end());
	for(int i = 1; i < size; i++){
		if(l[i] == l[i - 1]){
			l.erase(l.begin() + i);
			goto A;
		}
	}
	return l;
}

int main(void){
	vector<int> v = {5, 3, 5, 2, 3, 3, 9, 0, 123};
	for(int i : unique(v)){
		printf("%d ", i);
	}
	return 0;
}



