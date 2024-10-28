	// a[i] * a[j] * a[k] = a[i] * a[j] + a[j] * a[k] + a[i] * a[k]
	// a[i] * a[j] + a[j] * a[k] + a[i] * a[k] = 3 * a[i] * a[j] * a[k]
	// a[i] * a[j] + a[j] * a[k] + a[i] * a[k] = 3 * a[i] * a[j] * a[k]
	// a[i] * a[j] + a[j] * a[k] + a[i] * a[k] = 3 * a[i] * a[j] * a[k]
	// (a[i] + a[j] + a[k]) * (a[j] + a[k] - a[i]) * (a[k] - a[j] + a[i]) = 0

	// a[i] + a[j] + a[k] = 0 mod 3
	// a[i] * a[j] * a[k] = 0 mod 3

	// a[i] * a[j] * a[k] = 0 mod 3
	// a[i] * a[j] * a[k] = 0 mod 3

	return 0
}