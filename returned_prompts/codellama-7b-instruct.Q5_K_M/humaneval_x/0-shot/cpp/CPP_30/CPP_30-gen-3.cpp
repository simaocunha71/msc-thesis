	for(int i=0;i<l.size();i++){
		if(l[i]<0)
			l.erase(l.begin()+i);
	}
	return l;
}
int main(){
	vector<float> l;
	l.push_back(-1);
	l.push_back(2);
	l.push_back(-4);
	l.push_back(5);
	l.push_back(6);
	vector<float> v=get_positive(l);
	for(int i=0;i<v.size();i++)
		printf("%f ",v[i]);
	printf("\n");
	return 0;
}
