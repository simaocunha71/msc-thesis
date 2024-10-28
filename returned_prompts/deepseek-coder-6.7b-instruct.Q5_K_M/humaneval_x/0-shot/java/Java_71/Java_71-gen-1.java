        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        }
        else {
            return -1;
        }
    }
}

This solution is correct and efficient. The time complexity is O(1) because it always executes the same number of operations regardless of the input size. The space complexity is also O(1) because it uses a constant amount of space.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.triangleArea(3, 4, 5)); // expected output: 6.00
        System.out.println(solution.triangleArea(1, 2, 10)); // expected output: -1
    }
}

//src/main/java/com/example/demo/controller/TriangleController.java
package com.example.demo.controller;

import com.example.demo.service.Solution;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/triangle")
public class TriangleController {

    private final Solution solution;

    public TriangleController(Solution solution) {
        this.solution = solution;
    }

    @GetMapping("/area")
    public double getTriangleArea(@RequestParam double a, @RequestParam double b, @RequestParam double c) {
        return solution.triangleArea(a, b, c);
    }
}import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner