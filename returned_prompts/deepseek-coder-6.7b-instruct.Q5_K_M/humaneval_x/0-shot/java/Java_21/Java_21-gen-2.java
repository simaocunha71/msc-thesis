        List<Double> result = new ArrayList<>();
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        for (double num : numbers) {
            result.add((num - min) / (max - min));
        }
        return result;
    }
}

This solution first finds the minimum and maximum of the given list. Then it goes through each number in the list, subtracts the minimum, divides by the difference of the maximum and minimum, and adds to the result list.

This rescaling operation transforms the original list into a new one where each number is expressed as a ratio of its distance from the smallest number to the distance from the largest number, effectively normalizing the numbers to fall within the range [0, 1].
    */
}

//src/main/java/com/example/demo/DemoApplication.java
package com.example.demo;

import com.example.demo.solutions.Solution;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.Arrays;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);

		Solution solution = new Solution();
		System.out.println(solution.rescaleToUnit(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0)));
	}

}

//src/test/java/com/example/demo/DemoApplicationTests.java
package com.example.demo;

import com.example.demo.solutions.Solution;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class DemoApplicationTests {

	@Test
	void contextLoads() {
	}

