	int n = l.size();
	sort(l.begin(), l.end());
	int m = n/2;
	if(n%2 == 1)
		return l[m];
	else
		return (l[m-1]+l[m])/2;
}
int main(void){
	vector<float> l = {-10, 4, 6, 1000, 10, 20};
	printf("%.1f\n", median(l));
}
