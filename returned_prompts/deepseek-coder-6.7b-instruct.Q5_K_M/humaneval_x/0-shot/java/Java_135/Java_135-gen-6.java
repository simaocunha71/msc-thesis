    for (int i = 1; i < arr.size(); i++) {
        if (arr.get(i) < arr.get(i-1)) {
            return i-1;
        }
    }
    return -1;
}
}

This code will return the index of the first element in the list that is less than the element before it. If no such element exists, it will return -1.

Your original code was incorrect because it was returning the index of the first element that is greater than or equal to the previous element, which is not the same as the problem statement.

