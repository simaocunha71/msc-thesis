	sort(numbers.begin(),numbers.end());

	float min_diff = abs(numbers[0] - numbers[1]);
	float min_diff_numbers = numbers[0], min_diff_numbers_1 = numbers[1];

	for(int i = 1; i < numbers.size()-1; i++){
		if(abs(numbers[i] - numbers[i+1]) < min_diff)
		{
			min_diff = abs(numbers[i] - numbers[i+1]);
			min_diff_numbers = numbers[i];
			min_diff_numbers_1 = numbers[i+1];
		}
	}
	vector<float> result = {min_diff_numbers, min_diff_numbers_1};
	return result;
}

int main(){
	vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
	vector<float> result = find_closest_elements(numbers);
	for(int i = 0; i < result.size(); i++)
	{
		printf("%f ", result[i]);
	}
	return 0;
}










































































































































































































