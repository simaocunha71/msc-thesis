    // Edge case - check if the array is empty
    if (arr.size() == 0) {
        return Optional.empty();
    }

    // Initialize result and product of signs
    long result = 0;
    long prodSigns = 1;

    // Iterate over the array
    for (int i = 0; i < arr.size();