
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(j));
        if (distance < threshold) return true;
    }
}
return false;

Your solution here is very inefficient. It's O(n^2) which means it's quadratic in time complexity. You can optimize it to O(n) which is linear in time complexity. 

You can use a TreeSet to keep track of all the numbers you've seen so far. 
For each number in the list, you can use the lower method of TreeSet to find the greatest number which is less than the current number. 
If the difference between the current number and this greatest number is less than the threshold, then return true. 
If you can't find such a greatest number, that means the current number is the smallest number you've seen so far. You can use the ceiling method of TreeSet to find the smallest number which is greater than the current number. 
If the difference between the current number and this smallest number is less than the threshold, then return true. 

Here is the optimized code: 

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Set<Double> seen = new TreeSet<>();
    for (Double number : numbers) {
        Double lower = seen.lower(number);
        if (lower != null && number - lower < threshold) {
            return true;
        }
        Double ceiling = seen.ceiling(number);
        if (ceiling != null && ceiling - number < threshold) {
            return true;
        }
        seen.add(number);
    }
    return false;
}

Note that TreeSet is a sorted set, and it can be used to keep track of all the numbers you've seen so far. The lower method of TreeSet can be used to find the greatest number which is less than the given number, and the ceiling method of TreeSet can be used to find the smallest number which is greater than the