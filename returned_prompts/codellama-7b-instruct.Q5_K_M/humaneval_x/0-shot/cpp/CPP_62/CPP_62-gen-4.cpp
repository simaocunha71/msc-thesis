	int n = xs.size();
	vector<float> result(n-1);
	for(int i=1; i<n; i++){
		result[i-1] = xs[i]*i;
	}
	return result;


