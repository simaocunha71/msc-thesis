	for(int i = 0; i < l.size() - 1; i++){
		if(l[i] > l[i + 1]){
			for(int j = i + 1; j < l.size(); j++){
				if(l[j] < l[i]) return false;
			}
		}
		else if(l[i] < l[i + 1]){
			for(int j = i + 1; j < l.size(); j++){
				if(l[j] > l[i]) return false;
			}
		}
	}
	return true;
}
int main(){
	vector<float> l = {1, 2, 4, 20};
	printf("%d\n", monotonic(l));
	l = {1, 20, 4, 10};
	printf("%d\n",