    List<String> result = new ArrayList<>();
    for (String s : strings) {
        if (s.contains(substring)) {
            result.add(s);
        }
    }
    return result;
}
}

Answer:

The filterBySubstring method takes in a List of Strings and a String, and returns a List of Strings.
The method iterates through each string in the input list. If the string contains the given substring, it is added to the result list.
The method returns the result list after all strings have been checked.

Example usage:

List<String> strings = Arrays.asList("abc", "bacd", "cde", "array");
String substring = "a";
List<String> result = filterBySubstring(strings, substring);
System.out.println(result); // Output: ["abc", "bacd", "array"]

In this example, the filterBySubstring method is called with a list of strings ["abc", "bacd", "cde", "array"] and the substring "a". The result is a new list containing only the strings that contain the substring "a", which are ["abc", "bacd", "array"]. This list is then printed to the console.

The time complexity of the filterBySubstring method is O(n), where n is the number of strings in the input list. This is because the method iterates through each string in the list once. The space complexity is O(k), where k is the number of strings that contain the substring, as the result list may grow in size.

Overall, the filterBySubstring method provides a convenient way to filter a list of strings based on the presence of a specific substring, and can be used in various applications where such filtering is required.




































































































