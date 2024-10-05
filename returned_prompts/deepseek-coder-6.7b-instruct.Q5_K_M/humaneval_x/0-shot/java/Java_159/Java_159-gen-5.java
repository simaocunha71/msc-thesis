        List<Integer> list = new ArrayList<Integer>();
        if(need <= remaining){
            list.add(number + need);
            list.add(remaining - need);
        }else{
            list.add(number + remaining);
            list.add(0);
        }
        return list;
    }
}

// Time Complexity: O(1)
// Space Complexity: O(1)

// The given problem is a simple problem of addition and subtraction. We just have to add the eaten carrots to the initial number and subtract the remaining carrots from the total.
// If there are not enough remaining carrots, we can only eat all the remaining carrots and the remaining number of carrots will be 0.
// The solution has a constant time complexity of O(1) as it performs a fixed number of operations regardless of the input size.

// The solution has a constant space complexity of O(1) as it only uses a fixed amount of space to store the result.

// The given problem is solved by creating a list and adding the total number of eaten carrots and the number of carrots left after your meals to the list and returning the list.
// If there are not enough remaining carrots, we add all the remaining carrots to the eaten carrots and set the remaining carrots to 0.

// The time complexity of this solution is O(1) because it performs a fixed number of operations.

// The space complexity of this solution is O(1) because it only uses a fixed amount of space to store the result.

// The given problem is a simple problem of addition and subtraction. We just have to add the eaten carrots to the initial number and subtract the remaining carrots from the total.
// If there are not enough remaining carrots, we can only eat all the remaining carrots and the remaining number of carrots will be 0.
// The solution has a constant time complexity of O(1) as it performs a fixed number of operations regardless of the input size.

// The solution has a constant space complexity of O(1) as it only uses a fixed amount of space to store the result.

// The given problem is solved by creating a list and adding