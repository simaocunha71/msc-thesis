        return strings.stream()
                .filter(str -> str.startsWith(prefix))
                .collect(Collectors.toList());
    }
}

In this code, I used Java 8 streams to filter the list of strings. The filter method uses a lambda expression that checks if each string starts with the given prefix. If it does, it is included in the resulting list.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.filterByPrefix(List.of("abc", "bcd", "cde", "array"), "a"));
    }
}

/*
O:
[abc, array]
*/

//src/main/java/com/example/demo/Controller.java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class Controller {

    @GetMapping("/filterByPrefix")
    public List<String> filterByPrefix(@RequestParam List<String> strings, @RequestParam String prefix) {
        Solution solution = new Solution();
        return solution.filterByPrefix(strings, prefix);
    }
}

//src/test/java/com/example/demo/DemoApplicationTests.java
package com.example.demo;

import com.example.demo.Solution;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class DemoApplicationTests {

    @Test
    void contextLoads() {
    }

    @Test
    void testFilterByPrefix() {
        Solution solution = new Solution();
        assertEquals(List.of("abc", "array"), solution.filterByPrefix(List.of("abc", "b