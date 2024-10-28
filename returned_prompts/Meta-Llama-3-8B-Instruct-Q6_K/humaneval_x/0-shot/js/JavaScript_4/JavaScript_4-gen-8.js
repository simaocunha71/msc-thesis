Here is the Python solution for the problem:
```
def meanAbsoluteDeviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)
```
The function `meanAbsoluteDeviation` takes a list of numbers as an argument. It calculates the mean of the numbers and then calculates the absolute deviation of each number from the mean. The average of these deviations is returned as the Mean Absolute Deviation (MAD). This solution assumes that the input list is not empty and does not contain non-numeric values. 

Here is how you can test this function with the example given:
```
print(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```



Here is the JavaScript solution for the problem:
```
function meanAbsoluteDeviation(numbers) {
    let sum = 0;
    let mean = 0;
    for (let num of numbers) {
        sum += num;
    }
    mean = sum / numbers.length;
    let mad = 0;
    for (let num of numbers) {
        mad += Math.abs(num - mean);
    }
    return mad / numbers.length;
}
```
This function calculates the mean of the input numbers, then calculates the absolute deviation of each number from the mean, and finally returns the average of these deviations as the Mean Absolute Deviation (MAD). This solution assumes that the input array is not empty and does not contain non-numeric values. 

Here is how you can test this function with the example given:
```
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));  // Output: 1.0
```



Here is the Java solution for the problem:
```
public class Main {
    public static double meanAbsoluteDeviation(double[] numbers) {
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        double mean = sum / numbers.length;
        double mad = 0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.length;
    }

    public static void main(String[] args) {
        double[] numbers = {1.0, 2.0, 3.0, 4.0};
        System.out