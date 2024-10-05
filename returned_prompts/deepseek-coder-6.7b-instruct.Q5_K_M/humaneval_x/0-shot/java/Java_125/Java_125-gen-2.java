        if(txt.contains(" ")) {
            return Arrays.asList(txt.split(" "));
        } else if(txt.contains(",")) {
            return Arrays.asList(txt.split(","));
        } else {
            int count = 0;
            for(char c : txt.toCharArray()) {
                if(Character.isLowerCase(c) && (c - 'a') % 2 != 0) {
                    count++;
                }
            }
            return count;
        }
    }
}


A: Your code is almost correct, but you should return List<String> and int instead of Object. The method splitWords should be changed to return a List<String> when the input string contains whitespace or a comma. When the input string only contains lowercase letters, it should return an integer. 
Here is the modified code:
public List<String> splitWords(String txt) {
    if (txt.contains(" ")) {
        return Arrays.asList(txt.split(" "));
    } else if (txt.contains(",")) {
        return Arrays.asList(txt.split(","));
    } else {
        int count = 0;
        for (char c : txt.toCharArray()) {
            if (Character.isLowerCase(c) && (c - 'a') % 2 != 0) {
                count++;
            }
        }
        return Arrays.asList(String.valueOf(count));
    }
}

In the code above, Arrays.asList() is used to convert the array returned by split() method into a List. If the count of lowercase letters with odd order is more than zero, it is converted to a string and returned as a List with a single element.
Note: The method splitWords will return a List<String> when the input string contains a whitespace or a comma, and will return a List<String> with a single element that contains the count of lowercase letters with odd order when the input string contains only lowercase letters.

A: The problem with your code is that you're using the Arrays.asList() method incorrectly. This method is intended to create a List from