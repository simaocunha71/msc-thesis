	int size = 0;
	for(int i = 0; i < numbers.size(); i++) {
		if(i == 0 || numbers[i] != numbers[i - 1]) {
			numbers[size++] = numbers[i];
		}
	}
	return numbers.erase(numbers.begin() + size, numbers.end());
}


/*
From a vector of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.
>>> remove_duplicates({1, 2, 3, 2, 4})
{1, 3, 4}
*/

vector<int> remove_duplicates(vector<int> numbers){

	int size = 0;
	for(int i = 0; i < numbers.size(); i++) {
		if(i == 0 || numbers[i] != numbers[i - 1]) {
			numbers[size++] = numbers[i];
		}
	}
	return numbers.erase(numbers.begin() + size, numbers.end());
}

B:
int main()
{
    vector<int> v = {1,2,3,2,4};
    v.erase(remove_duplicates(v), v.end());
    for(auto e : v) printf("%d ", e);
    return 0;
}


C:

vector<int> remove_duplicates(vector<int> numbers){

	sort(numbers.begin(), numbers.end());
	int size = 0;
	for(int i = 0; i < numbers.size(); i++) {
		if(i == 0 || numbers[i] != numbers[i - 1]) {
			numbers[size++] = numbers[i];
		}
	}
	return numbers.erase(numbers.begin() + size, numbers.end());
}



D:
int main(){
    vector<int> v = {1,2,3,2,4};
    sort(v.begin(), v.end());
   