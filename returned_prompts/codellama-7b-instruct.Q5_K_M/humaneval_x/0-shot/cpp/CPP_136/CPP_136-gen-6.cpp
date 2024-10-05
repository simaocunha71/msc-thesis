	// check if lst is empty
	if(lst.size() == 0) return {0, 0};
	
	// initialize the max and min
	int max = INT_MIN;
	int min = INT_MAX;

	// iterate through the list
	for(int i = 0; i < lst.size(); i++){
		if(lst[i] < 0){ // is negative
			if(max < lst[i]){ // is larger than the current max
				max = lst[i];
			}
		}
		else{ // is positive
			if(min > lst[i]){ // is smaller than the current min
				min = lst[i];
			}
		}
	}

	// check if there is any negative
	if(max == INT_MIN){
		max = 0;
	}

	// check if there is any positive
	if(min == INT_MAX){
		min = 0;
	}

	// return the vector
	return {max, min};
}

int main(){
	vector<int> lst1 = {-1, -2, -3};
	vector<int> lst2 = {1, 2, 3};
	vector<int> lst3 = {0, 1, 2, 3};
	vector<int> lst4 = {};
	vector<int> lst5 = {0};

	vector<int> res1 = largest_smallest_integers(lst1);
	vector<int> res2 = largest_smallest_integers(lst2);
	vector<int> res3 = largest_smallest_integers(lst3);
	vector<int> res4 = largest_smallest_integers(lst4);
	vector<int> res5 = largest_smallest_integers(lst5);

	printf("Test 1: %d %d\n", res1[0], res1[1]);
	printf("Test 2: %d %d\n", res2[0], res2[1]);
	printf("Test 3: %d