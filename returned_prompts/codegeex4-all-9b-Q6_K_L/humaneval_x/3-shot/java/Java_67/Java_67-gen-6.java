
Your code has a logical error in the fruitDistribution function. You should split the string by "apples and" instead of "apples". Here is the correct solution:

public int fruitDistribution(String s, int n) {
    String[] fruit = s.split("apples and");
    int apples = Integer.parseInt(fruit[0].trim());
    int oranges = Integer.parseInt(fruit[1].split("oranges")[0].trim());
    int mango = n - apples - oranges;
    return mango;
}