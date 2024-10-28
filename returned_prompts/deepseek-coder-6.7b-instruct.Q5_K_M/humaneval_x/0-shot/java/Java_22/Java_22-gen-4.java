        List<Integer> integers = new ArrayList<Integer>();

        for (Object value : values) {
            if (value instanceof Integer) {
                integers.add((Integer) value);
            }
        }

        return integers;
    }
}

This is a simple solution using Java's built-in type checking mechanism. For each value in the input list, we check if it is an instance of Integer (`instanceof` keyword). If it is, we add it to the output list.

Please note that this solution assumes that you are using Java 8 or later, as it uses the List interface's `of` method. If you're using an older version of Java, you'll need to replace `List.of()` with `Arrays.asList()`.

Also, if you're using an older version of Java, you might need to replace `Map.of()` with a `HashMap<Object, Object>()` (or similar).

In the function signature, `List<Object> values` is used to accept a list of any objects.

This function will return a list of Integers from the input list. If there are no Integers in the list, it will return an empty list.

It is important to note that this function will not work correctly with floating point numbers, as these are not instances of Integer in Java.

I hope this helps clarify the problem and the solution.

Please let me know if you have any other questions.
