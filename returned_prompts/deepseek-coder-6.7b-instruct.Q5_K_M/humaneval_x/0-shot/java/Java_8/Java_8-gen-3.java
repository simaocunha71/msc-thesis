        int sum = 0;
        int product = 1;
        for(Integer num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}

Explanation:
The function sumProduct takes a list of integers as an argument. It first initializes two variables sum and product to 0 and 1 respectively. Then it iterates over the input list and for each number, it adds the number to sum and multiplies product by the number. Finally, it returns a list containing sum and product as the result.

Testing the function with given test cases:

sumProduct(List.of())
Output: [0, 1]

sumProduct(Arrays.asList(1, 2, 3, 4))
Output: [10, 24]

This solution has a time complexity of O(n) as it iterates over the list of integers once.

*/

// Explanation:
// The function sumProduct takes a list of integers as an argument. It first initializes two variables sum and product to 0 and 1 respectively. Then it iterates over the input list and for each number, it adds the number to sum and multiplies product by the number. Finally, it returns a list containing sum and product as the result.

// Testing the function with given test cases:

// sumProduct(List.of())
// Output: [0, 1]

// sumProduct(Arrays.asList(1, 2, 3, 4))
// Output: [10, 24]

// This solution has a time complexity of O(n) as it iterates over the list of integers once.

// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
// }
//