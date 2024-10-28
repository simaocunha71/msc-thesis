        Map<String, Integer> map = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            Integer count = map.get(word);
            if (count == null) {
                count = 0;
            }
            map.put(word, count + 1);
        }

        int max = 0;
        for (Integer value : map.values()) {
            if (value > max) {
                max = value;
            }
        }

        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

*/

//src/main/java/com/example/demo/controllers/MainController.java
package com.example.demo.controllers;

import com.example.demo.models.Question;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Random;

@RestController
public class MainController {

    private List<Question> questions = new ArrayList<>();

    @GetMapping("/questions")
    public ResponseEntity<List<Question>> getQuestions() {
        return new ResponseEntity<>(questions, HttpStatus.OK);
    }

    @PostMapping("/questions")
    public ResponseEntity<List<Question>> addQuestion(@RequestBody Question question) {
        questions.add(question);
        return new ResponseEntity<>(questions, HttpStatus.CREATED);
    }

    @PostMapping("/questions/multiple")
    public ResponseEntity<List<Question>> addQuestions(@RequestBody List<Question> newQuestions) {
        questions.addAll(newQuestions);
        return new ResponseEntity<>(questions, HttpStatus.CREATED);
    }

    @