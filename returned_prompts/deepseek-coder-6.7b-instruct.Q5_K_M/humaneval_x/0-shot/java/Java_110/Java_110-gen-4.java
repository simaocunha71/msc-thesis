        int odd_count1 = 0;
        int odd_count2 = 0;

        for (Integer num : lst1) {
            if (num % 2 != 0) {
                odd_count1++;
            }
        }

        for (Integer num : lst2) {
            if (num % 2 != 0) {
                odd_count2++;
            }
        }

        if (odd_count1 > odd_count2) {
            return "NO";
        }

        return "YES";
    }
}

Explanation:
Firstly, we count the number of odd numbers in both lst1 and lst2.
Then, we compare the count of odd numbers in lst1 with the count of odd numbers in lst2.
If the number of odd numbers in lst1 is more than the number of odd numbers in lst2, we cannot make all the numbers in lst1 to be even by exchanging elements from lst1 and lst2. So we return "NO".
Otherwise, we can make all the numbers in lst1 to be even by exchanging elements from lst1 and lst2. So we return "YES".

The time complexity of this solution is O(n) and the space complexity is O(1), where n is the size of the input lists.
*/

//src/main/java/com/example/demo/controller/ExchangeController.java
package com.example.demo.controller;

import com.example.demo.service.ExchangeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/exchange")
public class ExchangeController {

    @Autowired
    private ExchangeService exchangeService;

    @PostMapping
    public String exchange(@RequestBody List<Integer> lst1, @RequestBody List<