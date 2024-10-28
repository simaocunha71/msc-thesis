	for(int i = 0; i < l.size()-1; i++){
		if(l[i] > l[i+1]){
			if(l[i+1] == l[i+2]){
				return true;
			} else {
				return false;
			}
		}
		if(l[i] < l[i+1]){
			if(l[i+1] == l[i+2]){
				return true;
			} else {
				return false;
			}
		}
		if(l[i] == l[i+1]){
			continue;
		}
	}
	return false;
}
int main(){
	vector<float> l;
	l.push_back(1);
	l.push_back(2);
	l.push_back(4);
	l.push_back(20);
	cout << monotonic(l) << endl;
	return 0;
}
