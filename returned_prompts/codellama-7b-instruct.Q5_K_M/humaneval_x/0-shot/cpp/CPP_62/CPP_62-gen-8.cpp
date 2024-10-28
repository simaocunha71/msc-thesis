	int n = xs.size();
	vector<float> ys(n - 1);
	for(int i = 1; i < n; i++)
		ys[i - 1] = (i + 1) * xs[i];
	return ys;
}
