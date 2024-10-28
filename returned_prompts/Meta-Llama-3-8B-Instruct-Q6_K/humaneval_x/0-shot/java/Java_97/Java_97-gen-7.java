    return (a % 10) * (b % 10);
}

// Test the solution
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.multiply(148, 412));  // Output: 16
        System.out.println(solution.multiply(19, 28));  // Output: 72
        System.out.println(solution.multiply(2020, 1851));  // Output: 0
        System.out.println(solution.multiply(14, -15));  // Output: 20
    }
}