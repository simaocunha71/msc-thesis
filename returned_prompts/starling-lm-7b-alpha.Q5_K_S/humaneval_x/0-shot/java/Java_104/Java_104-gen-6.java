
    // Sort input array
    Collections.sort(x);

    // Create a new array to store results
    List<Integer> result = new ArrayList<>();

    for (int i = 0; i < x.size(); i++) {
        // Check if any of the digits in current element is even
        if (checkEven(x.get(i))) {
            continue A;
        }

        // Check if result array contains the element
        if (!result.contains(x.get(i))) {
            result.add(x.get(i));
        }
    }

    return result;
    }

    /**
    Check if any of the digits in the number is even.

    @param  {Integer} number The number to be checked.
    @return {Boolean} True if any of the digits is even, false otherwise.
    */
    private boolean checkEven(int number) {
    while (number != 0) {
        int rem = number % 10;
        if (rem % 2 == 0) {
            return true;
        }
        number /= 10;
    }
    return false;
    }

}







































































































































































































































