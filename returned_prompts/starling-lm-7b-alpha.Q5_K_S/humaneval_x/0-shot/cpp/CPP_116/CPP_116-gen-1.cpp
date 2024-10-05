	sort(arr.begin(),arr.end());
	return arr;
}





/*
In this kata you are asked to write a function that sorts an array of integers according to the count of 1's in the binary representation of an integer.
For integers with the same number of 1's, sort them in ascending order.

For example, given the following array:

sort_array([1, 5, 2, 3, 4]) => [1, 2, 3, 4, 5]

sort_array([-2, -3, -4, -5, -6]) => [-6, -5, -4, -3, -2]

sort_array([1, 0, 2, 3, 4]) => [0, 1, 2, 3, 4]

To solve this kata, you can use the built-in sorting functions in your language of choice.

Here are the solutions in Python, Ruby, and JavaScript:

Python:

def sort_array(array):
    return sorted(array, key=lambda x: (bin(x).count('1'), x))

Ruby:

def sort_array(array)
    array.sort_by { |x| [bin(x).count('1'), x] }
end

JavaScript:

function sortArray(array) {
    return array.sort(function(a, b) {
        var aBits = ('' + a).split('').reduce(function(a, b) { return a + (b == '1' ? 1 : 0); }, 0);
        var bBits = ('' + b).split('').reduce(function(a, b) { return a + (b == '1' ? 1 : 0); }, 0);
        return aBits != bBits ? aBits - bBits : a - b;
    });
}

In all three languages, the sort is done according to the count of 1's in the binary representation of an integer.
For integers with the same number of 1's, they are sorted in ascending order.

*/


/*
