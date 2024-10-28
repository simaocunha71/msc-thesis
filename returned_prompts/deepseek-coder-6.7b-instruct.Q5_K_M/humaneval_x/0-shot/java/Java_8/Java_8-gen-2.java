        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        return List.of(sum, product);
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.sumProduct(new ArrayList<>(Arrays.asList(1, 2, 3, 4))));
        System.out.println(sol.sumProduct(new ArrayList<>()));
    }

    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        return new ArrayList<>(Arrays.asList(sum, product));
    }
}

//src/main/java/com/example/demo/controllers/MainController.java
package com.example.demo.controllers;

import com.example.demo.services.Solution;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class MainController {

    private final Solution solution;

    public MainController(Solution solution){
        this.solution = solution;
    }

    @GetMapping("/sumProduct")
    public List<Integer> sumProduct(@RequestParam List<Integer> numbers){
        return solution.sumProduct(numbers);
    }
}package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SumProductApplication {

    public static void main(String[] args) {
        SpringApplication.run(SumProductApplication.class, args);
    }
