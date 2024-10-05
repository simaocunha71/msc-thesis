        List<Integer> result = new ArrayList<Integer>();

        if(need <= remaining){
            result.add(number + need);
            result.add(remaining - need);
        } else {
            result.add(number + remaining);
            result.add(0);
        }

        return result;
    }
}

The solution works by checking if the need is less than or equal to the remaining carrots. If it is, you can eat the remaining carrots, and there will be some left. If not, you can't eat the remaining carrots, and all you eat is what you have.
The total number of eaten carrots is the current number of carrots eaten plus the number of carrots that need to be eaten. The number of carrots left is the remaining carrots minus the number of carrots that need to be eaten.
If there are not enough remaining carrots, the number of carrots left after your meals is 0.
The time complexity of the solution is O(1) because it performs a constant number of operations, regardless of the size of the input.
The space complexity of the solution is O(1) because it uses a constant amount of space to store the result.
*/

//src/main/java/com/example/demo/controller/RabbitController.java
package com.example.demo.controller;

import com.example.demo.service.RabbitService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/rabbit")
public class RabbitController {

    @Autowired
    private RabbitService rabbitService;

    @GetMapping("/eat/{number}/{need}/{remaining}")
    public ResponseEntity<List<Integer>> eat(@PathVariable int number, @PathVariable int need, @PathVariable int remaining){
        return ResponseEntity.ok(rabbitService.eat(number, need, remaining));
    }
}

//src/main/java/com/example/demo/service