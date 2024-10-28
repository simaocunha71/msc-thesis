    List<Integer> result = new ArrayList<>();
    int level = 1;
    int stones = n;
    while (stones > 0) {
        result.add(stones);
        if (level % 2 == 1) {
            stones = (int) Math.ceil(stones / 2.0) * 2 + 1;
        } else {
            stones = (int) Math.ceil(stones / 2.0) * 2;
        }
        level++;
    }
    return result;
}  // This is the solution in Java.
// It uses a list to store the number of stones in each level. It starts with n stones.
// For each level, it calculates the number of stones in the next level by dividing the current
// number of stones by 2 and rounding up to the nearest integer, then multiplying by 2 and adding 1
// if the current level is odd, or simply multiplying by 2 if the current level is even.
// It continues this process until there are no more stones left.
// Finally, it returns the list of numbers of stones in each level. 







