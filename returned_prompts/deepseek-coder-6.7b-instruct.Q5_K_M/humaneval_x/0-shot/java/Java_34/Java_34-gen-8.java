        Set<Integer> set = new HashSet<>(l);
        List<Integer> result = new ArrayList<>(set);
        Collections.sort(result);
        return result;
    }

    public static void main((String[] args) {
        Solution s = new Solution();
        System.out.println(s.unique(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123)));
    }
}

The main part of the code is in the `unique` function. We start by converting the list into a `Set` which automatically removes any duplicate elements as Sets can only contain unique elements. We then convert this `Set` back into a `List`. Finally, we sort this list before returning it.

Please note that the main method is also included. It creates a new instance of the `Solution` class and calls the `unique` method with a list of integers. The result is then printed to the console.

This solution assumes that the input list contains only integers. If the list can contain other types of objects, you would need to modify the code to handle these cases.

Also, please note that the main method should be placed in a class named 'Main' or any other class with a `public static void main(String[] args)` method. It cannot be placed in a class named 'Solution' as you've mentioned in your question.
