        List<String> result = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int start = 0;

        for (int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                stack.pop();
            }
            sb.append(c);
            if (stack.isEmpty()) {
                result.add(sb.substring(start, i + 1));
                start = i + 1;
                sb = new StringBuilder();
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.separateParenGroups("(  )  (( ))  (( )( ))"));
    }
}

*/

import java.util.*;

public class Solution {
    public List<String> separateParenGroups(String s) {
        List<String> res = new ArrayList<>();
        int start = 0;
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                stack.pop();
            }
            if (stack.isEmpty()) {
                res.add(s.substring(start, i + 1));
                start = i + 1;
            }
        }
        return res;
    }
}

//src/main/java/com/example/demo/controller/HelloController.java
package com.example.demo.controller;

import com.example.demo.service.HelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.