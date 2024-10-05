    vector<int> res;
    int x = 1;
    while (x <= n) {
        res.push_back(x);
        if (x % 2 == 0) {
            x += 2;
        } else {
            x += 1;
        }
    }
    return res;
}


#if 0
/*
Given an array of integers, remove all the elements with a value of 0, in place.
The array size will be at least one element.

Examples:
>>> remove_zeroes([1,0,2,0,3,0])
[1,2,3]
>>> remove_zeroes([1,2,3])
[1,2,3]
>>> remove_zeroes([])
[]
*/

void remove_zeroes(int *nums, int size) {
    int i = 0;
    for (; i < size; i++) {
        if (nums[i] != 0) {
            break;
        }
    }
    if (i == size) {
        return;
    }
    int j = i;
    for (; j < size; j++) {
        if (nums[j] == 0) {
            for (; j < size - 1; j++) {
                nums[j] = nums[j + 1];
            }
            size--;
            j--;
        }
    }
}
#endif


#if 0
/*
Given a string, find the first non-repeating character and return it.
If there are no non-repeating characters, return an asterisk (*).

Examples:
>>> first_non_repeating_char("Programming")
'P'
>>> first_non_repeating_char("aaabbbccc")
'*'
>>> first_non_repeating_char("aaabbbcccddde")
'e'
>>> first_non_repeating_char("aaabbbcccdddeee")
'd'
>>> first_non_repeating_char("aaabbbcccddeee")
