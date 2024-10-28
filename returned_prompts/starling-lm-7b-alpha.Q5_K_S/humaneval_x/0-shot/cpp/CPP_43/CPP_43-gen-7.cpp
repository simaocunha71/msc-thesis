	for(int i = 0; i < l.size(); i++)
		for(int j = i + 1; j < l.size(); j++)
			if(l[i] + l[j] == 0)
				return true;
	return false;
}



/*
The code you've provided defines a function called pairs_sum_to_zero that
takes a vector of integers as an input and returns true if there are two
distinct elements in the vector that sum to zero, and false otherwise.

The function works by iterating over all possible pairs of distinct elements
in the input vector using nested for loops. For each pair of elements, it checks
if their sum is equal to zero. If the sum is zero, the function immediately
returns true, indicating that a pair of elements that sum to zero has been found.
If no such pair is found after examining all possible pairs, the function
returns false.

The function can be used as follows:

To call the function, you can use the following syntax:
result = pairs_sum_to_zero(vector);

Here, result is a boolean variable that will store the result of the function
call. The vector is the input vector of integers on which the function will be called.

After calling the function, you can check the value of the result variable to
determine whether the function returned true or false. If the result variable is true,
it means that there are two distinct elements in the input vector that sum to zero.
If the result variable is false, it means that no such pair of elements exists in the input vector.

For example, if you call the function with the input vector {1, 3, 5, 0}, the function will return false,
because there are no two distinct elements in the vector that sum to zero. On the other hand,
if you call the function with the input vector {2, 4, -5, 3, 5, 7}, the function will return true,
because there are two distinct elements in the vector (specifically, -5 and 3) that sum to zero.

To use the function in your own code, you can copy and paste the provided code into your program.
Make sure to include the necessary header file