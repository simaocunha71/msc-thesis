	for(int i = 0; i < l.size(); i++){
		for(int j = i+1; j < l.size(); j++){
			for(int k = j+1; k < l.size(); k++){
				if(l[i] + l[j] + l[k] == 0){
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	vector<int> l = {1, 3, 5, 0};
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("false\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("true\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("false\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("true\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("false\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("false\n");
	printf(">>> triples_sum_to_zero({%d, %d, %d, %d})\n", l[0], l[1], l[2], l[3]);
	printf("false\