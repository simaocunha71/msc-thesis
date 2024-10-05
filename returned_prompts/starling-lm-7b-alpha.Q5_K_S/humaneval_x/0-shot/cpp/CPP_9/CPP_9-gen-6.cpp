	int i, n, max, max_number;
	vector<int> result;
	result.push_back(numbers[0]);
	for (i = 1; i < numbers.size(); i++) {
		max_number = numbers[i];
		for (n = i; n >= 0; n--) {
			if (max_number < numbers[n]) {
				max_number = numbers[n];
			}
		}
		result.push_back(max_number);
	}
	return result;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    for (int i: rolling_max(numbers)) {
        printf("%d ", i);
    }
    return 0;
}

static char* const __usage_msg = "Usage: %s [options]\n";

static void __show_help(FILE* out, int argc, char** argv) {
    if (argc != 1) {
        fprintf(out, __usage_msg, argv[0]);
        fprintf(out, "\t-h, --help\t\tShow help\n");
    }
}

int main(int argc, char** argv) {
    __show_help(stdout, argc, argv);
    return 0;
}
































































































































































