	if (n == 1) return 1;
	if (n == 2) return 2;
	return 2*starts_one_ends(n-1);
}

