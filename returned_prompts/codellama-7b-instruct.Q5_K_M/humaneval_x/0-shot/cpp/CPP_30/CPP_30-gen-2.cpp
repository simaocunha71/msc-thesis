	for(int i = 0; i < l.size(); i++){
		if(l[i] < 0)
			l.erase(l.begin() + i);
	}
	return l;
}
int main(){
	vector<float> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
	vector<float> p = get_positive(l);
	for(int i = 0; i < p.size(); i++)
		printf("%.0f ", p[i]);
	return 0;
}

