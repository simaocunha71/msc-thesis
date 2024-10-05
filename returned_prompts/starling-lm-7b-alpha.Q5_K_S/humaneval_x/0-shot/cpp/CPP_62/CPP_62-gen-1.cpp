	vector<float> result;
	result.resize(xs.size());
	if(xs.size() < 2) return result;
	result[0] = xs[1];
	for(int i=1; i<xs.size()-1; ++i){
		result[i] = result[i-1] + (i+1) * xs[i+1];
	}
	result[result.size()-1] = xs[result.size()-2] * (xs.size()-1);
	return result;
}
int main(){
	vector<float> xs = {3, 1, 2, 4, 5};
	printf(">>> derivative({3, 1, 2, 4, 5})\n");
	vector<float> result = derivative(xs);
	for(int i=0; i<result.size(); ++i){
		printf("%f", result[i]);
		if(i < result.size()-1) printf(", ");
		else printf("\n");
	}
	xs = {1, 2, 3};
	printf(">>> derivative({1, 2, 3})\n");
	result = derivative(xs);
	for(int i=0; i<result.size(); ++i){
		printf("%f", result[i]);
		if(i < result.size()-1) printf(", ");
		else printf("\n");
	}
	return 0;
}


























































































































































