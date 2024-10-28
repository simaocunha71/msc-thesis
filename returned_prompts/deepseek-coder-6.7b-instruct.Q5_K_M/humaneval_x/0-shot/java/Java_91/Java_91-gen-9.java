        int count = 0;
        String[] sentences = S.split("[.?!]");

        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                count++;
            }
        }

        return count;
    }
}

This solution works by splitting the input string into sentences using the split method. It then iterates over each sentence and checks if it starts with the word "I". If it does, it increments the count of boredoms. Finally, it returns the count.

This solution assumes that the input string only contains words separated by '.', '?' or '!' and that there are no other punctuation marks. If this is not the case, you might need to adjust the split pattern to handle these cases.

Also, this solution is case sensitive. If you want to count "i" as a boredom as well, you will need to adjust the condition to check for both "I" and "i".

Here is a test:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.isBored("Hello world")); // Expected output 0
    System.out.println(solution.isBored("The sky is blue. The sun is shining. I love this weather")); // Expected output 1
    System.out.println(solution.isBored("I am bored. i think i should go home. I sleep all day")); // Expected output 2
}
```

In this test, the first sentence has no boredom, the second has one and the third has two.
    */
}

//src/main/java/com/example/demo/models/User.java
package com.example.demo.models;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username")
    private String username;

    @Column(name = "password")
