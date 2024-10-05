        String[] validExtensions = {"txt", "exe", "dll"};
        String[] fileParts = file_name.split("\\.");

        if (fileParts.length != 2) {
            return "No";
        }

        String namePart = fileParts[0];
        String extension = fileParts[1];

        if (namePart.length() == 0 || !Character.isLetter(namePart.charAt(0))) {
            return "No";
        }

        int digitCount = 0;
        for (char c : namePart.toCharArray()) {
            if (Character.isDigit(c)) {
                digitCount++;
            }
        }

        if (digitCount > 3) {
            return "No";
        }

        if (Arrays.asList(validExtensions).contains(extension)) {
            return "Yes";
        } else {
            return "No";
        }
    }
}


A: Here's the corrected version of your code:

```java
import java.util.*;
import java.lang.*;

class Solution {

    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
      */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }
}
```

```java
import java.util.*;
import java.lang