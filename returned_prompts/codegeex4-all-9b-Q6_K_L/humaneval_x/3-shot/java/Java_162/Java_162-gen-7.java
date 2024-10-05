
Java 8
The first question can be solved using a more functional approach by using the IntStream.range() function to create an integer stream of all the indices in the list. We then map each index to the difference between the value at that index and the value at the next index, and finally use the anyMatch() function to check if any of these differences are smaller than the threshold.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    return IntStream.range(0, numbers.size() - 1)
            .anyMatch(i -> Math.abs(numbers.get(i) - numbers.get(i + 1)) < threshold);
}

The second question can be solved using a more functional approach by using the IntStream.range() function to create an integer stream of all the indices in the list. We then map each index to the value at that index, and finally use the reduce() function to concatenate all the values into a single string.
public List<String> separateParenGroups(String paren_string) {
    return IntStream.range(0, paren_string.length())
            .filter(i -> paren_string.charAt(i) == '(')
            .mapToObj(i -> paren_string.substring(i, paren_string.indexOf(')', i) + 1))
            .collect(Collectors.toList());
}

The third question can be solved using the Math.floor() function to get the integer part of the number, and then subtracting that from the number to get the decimal part.
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

The fourth question can be solved using the MessageDigest class from the java.security package. We first create a new MessageDigest object using the getInstance() function, and then update the digest with the bytes of the input string. We then digest the bytes to get the hash, and convert the hash to a hexadecimal string using a BigInteger object and the toString() function. Finally, we pad the string with leading zeros to make it 32 characters long.
public Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {
   