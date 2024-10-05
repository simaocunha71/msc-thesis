	int c=0, i, j, k, l, m, sum, sign;
	for (i=0; i<n.size(); i++) {
		sign = 0;
		sum = 0;
		for (j=0; j<n[i]; j++) {
			if (n[i] < 0) {
				sign++;
				n[i] *= -1;
			}
			sum += n[i]%10;
			n[i]/=10;
		}
		if (sum > 0)
			c++;
	}
	return c;
}














/*
Write a function count_nums which takes a vector of inte