    String str1 = lst.get(0);
    String str2 = lst.get(1);
    int count = 0;

    for (int i = 0; i < str1.length(); i++) {
      if (str1.charAt(i) == '(') {
        count++;
      } else if (str1.charAt(i) == ')') {
        count--;
        if (count < 0) {
          return "No";
        }
      }
    }

    for (int j = 0; j < str2.length(); j++) {
      if (str2.charAt(j) == '(') {
        count++;
      } else if (str2.charAt(j) == ')') {
        count--;
        if (count < 0) {
          return "No";
        }
      }
    }

    if (count != 0) {
      return "No";
    }

    return "Yes";
  }
}

This solution works by iterating over each string and keeping track of the count of open parentheses. If we encounter a close parentheses and the count is less than 1, we return "No" since this means there is a closing parenthesis without a corresponding opening one. At the end of both iterations, if the count is not 0, we return "No" as there might be unbalanced parentheses. If none of these conditions are met, we return "Yes" indicating that the strings can be concatenated to form a balanced parentheses string.

The time complexity of this solution is O(n), where n is the length of the longest string, as we are iterating over each string once. The space complexity is O(1), as we are only using a constant amount of space to store the count and the strings.
      */

}

//src/main/java/com/example/demo/controller/SolutionController.java
package com.example.demo.controller;

import com.example.demo.model.Solution;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
