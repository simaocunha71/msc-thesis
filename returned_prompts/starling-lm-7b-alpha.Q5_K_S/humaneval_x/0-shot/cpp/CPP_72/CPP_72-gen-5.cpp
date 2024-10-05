	if (q.size() % 2 != 0)
		return false;
	else {
		int i, j;
		for (i = 0, j = q.size() - 1; i < j; i++, j--) {
			if (q[i] != q[j])
				return false;
		}
	}
	int sum = 0;
	for (int i = 0; i < q.size(); i++) {
		sum += q[i];
	}
	if (sum > w)
		return false;
	else
		return true;
}
int main() {
	int w;
	vector<int> q;
	scanf("%d", &w);
	for (int i = 0; i < w; i++) {
		int tmp;
		scanf("%d", &tmp);
		q.push_back(tmp);
	}
	if (will_it_fly(q, w))
		printf("true\n");
	else
		printf("false\n");
	return 0;
}












































































































































































































































