        List<Integer> results = new ArrayList<>();
        String[] groups = paren_string.split(" ");

        for (String group : groups) {
            int maxDepth = 0;
            int currentDepth = 0;

            for (char c : group.toCharArray()) {
                if (c == '(') {
                    currentDepth++;
                    if (currentDepth > maxDepth) {
                        maxDepth = currentDepth;
                    }
                } else if (c == ')') {
                    currentDepth--;
                }
            }

            results.add(maxDepth);
        }

        return results;
    }
}

This solution works by iterating over each character in each group of parentheses. The depth of the current nesting is incremented whenever an opening parenthesis is encountered and decremented whenever a closing parenthesis is encountered. The maximum depth encountered is stored in `maxDepth` and added to the results list.

It then returns the list of maximum depths for each group of parentheses.

Note that this solution assumes that the input string is well-formed and contains only parentheses and spaces. If the input string might not be well-formed, additional error checking would be necessary.
    */
}

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        List<Integer> results = solution.parseNestedParens("(()()) ((())) () ((())()())");
        System.out.println(results);  // Output: [2, 3, 1, 3]
    }
}

//src/main/java/com/example/demo/model/User.java
package com.example.demo.model;

import java.util.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.