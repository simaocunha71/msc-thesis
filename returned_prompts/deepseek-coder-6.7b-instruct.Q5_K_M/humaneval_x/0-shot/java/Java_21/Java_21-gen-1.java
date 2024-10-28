        List<Double> rescaled = new ArrayList<>();
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        for(double number : numbers) {
            rescaled.add((number - min) / (max - min));
        }
        return rescaled;
    }
}

This solution firstly finds the minimum and maximum elements in the input list. Then it transforms each element in the list by subtracting the minimum from it and dividing the result by the difference between the maximum and the minimum. This will scale the elements to the range [0,1].

This approach is correct because it ensures that the smallest number in the list becomes 0 and the largest number becomes 1. This is a common operation in data science and machine learning where data needs to be scaled to a fixed range.

Also, this solution uses Java 8 features like Lambda expressions and method references which are part of the Java 8 API.
    */
}

//src/main/java/com/example/demo/controllers/MainController.java
package com.example.demo.controllers;

import com.example.demo.services.MainService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/api")
public class MainController {

    private final MainService mainService;

    @Autowired
    public MainController(MainService mainService) {
        this.mainService = mainService;
    }

    @GetMapping(value = "/hello")
    public String hello() {
        return mainService.hello();
    }
}

//src/main/java/com/example/demo/services/MainService.java
package com.example.demo.services;

import com.example.demo.models.User;
import com.example.demo.repositories.UserRepository;
import com.example.demo.services.impl.MainServiceImpl;