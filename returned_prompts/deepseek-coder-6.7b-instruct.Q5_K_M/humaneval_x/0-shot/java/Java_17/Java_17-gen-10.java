        List<Integer> noteLengths = new ArrayList<>();
        String[] notes = string.split(" ");

        for(String note : notes) {
            switch(note) {
                case "o":
                    noteLengths.add(4);
                    break;
                case "o|":
                    noteLengths.add(2);
                    break;
                case ".|":
                    noteLengths.add(1);
                    break;
            }
        }
        return noteLengths;
    }
}

*/

//src/main/java/com/example/demo/controller/SolutionController.java
package com.example.demo.controller;

import com.example.demo.model.Solution;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class SolutionController {

    Solution solution = new Solution();

    @GetMapping("/parseMusic")
    public List<Integer> parseMusic(@RequestParam(value = "music") String music) {
        return solution.parseMusic(music);
    }
}

//src/test/java/com/example/demo/DemoApplicationTests.java
package com.example.demo;

import com.example.demo.model.Solution;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class DemoApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
	public void testParseMusic() {
		Solution solution = new Solution();

		List<Integer> expected = Arrays.asList(4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4);
		