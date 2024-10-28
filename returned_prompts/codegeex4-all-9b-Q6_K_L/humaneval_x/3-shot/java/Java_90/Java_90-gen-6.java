
The Solution class is not necessary for your code and can be removed. The methods can be static and can be placed in an anonymous class or any other class.
The Solution class can be removed:
public static boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

The method name should start with a lower case letter:
public static boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

The method name should be more descriptive:
public static boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

The method name should be more descriptive:
public static boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true