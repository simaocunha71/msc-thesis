	vector<float> temp;
	float a;
	for(int i = 1; i < xs.size(); i++){
		a = i * xs[i];
		temp.push_back(a);
	}
	return temp;
}



