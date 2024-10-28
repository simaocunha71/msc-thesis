	int l = 0, r = arr.size() - 1;
	int ret = 0;

	while (l < r) {
		if (arr[l] == arr[r]) {
			l++;
			r--;
			continue;
		}

		int cnt = 0;
		for (int i = l; i <= r; i++) {
			if (arr[i] != arr[l]) {
				cnt++;
			}
			if (arr[i] != arr[r]) {
				cnt++;
			}
		}
		ret = max(ret, cnt);
		if (arr[l] != arr[r]) {
			l++;
		}
		r--;
	}
	return ret;
}

int main() {
	vector<int> arr = { 1,2,3,5,4,7,9,6 };
	printf("%d\n", smallest_change(arr));
	return 0;
}























































































































































































































































