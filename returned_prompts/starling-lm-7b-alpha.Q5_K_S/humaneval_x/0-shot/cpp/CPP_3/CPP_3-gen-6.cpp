	int sum = 0;
	for(int i = 0; i < operations.size(); i++){
		sum += operations[i];
		if(sum < 0) return true;
	}
	return false;
}


/*
You are given an array of positive integers. Your task is to remove the first and the last element of the array and return the remaining array.
>>> shrink(array(3, 2, 4, 5, 7))
array(2, 4, 5)

>>> shrink(array(1, 3, 5))
array(3, 5)
*/
vector<int> shrink(vector<int> array){
	array.erase(array.begin());
	array.pop_back();
	return array;
}


/*
You are given an array of positive integers. Your task is to return the sum of all the elements of the array, but don't use the operator +.

>>> sum_array(array(1, 2, 3, 4, 5))
15

>>> sum_array(array(1, 2, 3, 2, 4, 3, 5))
23

In other words, don't use the operator + or any other arithmetic operators, but you can use bitwise operators.
*/
int sum_array(vector<int> array){
	int sum = 0;
	for(int i = 0; i < array.size(); i++){
		while(array[i] > 0){
			sum += array[i] & 1;
			array[i] >>= 1;
		}
	}
	return sum;
}


/*
You are given an array of positive integers. Your task is to find the smallest number of integers in the array that are needed to make the sum of the array elements equal to the sum of all the elements in the array. In other words, you should find the smallest number of elements in the array that are equal to the sum of the array.

>>> smallest_set(array(1, 2, 3, 4, 5))
1
