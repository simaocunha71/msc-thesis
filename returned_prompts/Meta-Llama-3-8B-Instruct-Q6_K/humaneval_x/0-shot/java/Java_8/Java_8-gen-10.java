    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;

        for (int num : numbers) {
            sum += num;
            product *= num;
        }

        return Arrays.asList(sum, product);
    }
}
Explanation:
The given problem is asking to create a method that takes a list of integers as input and returns a list containing the sum and product of all the integers in the list. If the input list is empty, the sum should be 0 and the product should be 1.

In this solution, we use a for-each loop to iterate over the list of integers. We initialize two variables, `sum` and `product`, to 0 and 1 respectively. Then, we add each integer to the `sum` and multiply each integer with the `product`.

Finally, we return a list containing the `sum` and `product` as a tuple. If the input list is empty, the `sum` will remain 0 and the `product` will remain 1, which is the expected result. For example, if the input list is `List.of(1, 2, 3, 4)`, the output will be `[10, 24]`, which is the sum and product of the integers in the list. If the input list is `List.of()`, the output will be `[0, 1]`, which is the expected result.