        int sum1 = 0;
        int sum2 = 0;

        for (String s : lst1)
            sum1 += s.length();

        for (String s : lst2)
            sum2 += s.length();

        if (sum1 < sum2)
            return lst1;
        else if (sum1 > sum2)
            return lst2;
        else
            return lst1;
    }
}

This code defines a function totalMatch that calculates the total number of characters in a list of strings. It compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list.

*/

// Tests
List<String> lst1 = Arrays.asList();
List<String> lst2 = Arrays.asList();
System.out.println(totalMatch(lst1, lst2)); // []

lst1 = Arrays.asList("hi", "admin");
lst2 = Arrays.asList("hI", "Hi");
System.out.println(totalMatch(lst1, lst2)); // ["hI", "Hi"]

lst1 = Arrays.asList("hi", "admin");
lst2 = Arrays.asList("hi", "hi", "admin", "project");
System.out.println(totalMatch(lst1, lst2)); // ["hi", "admin"]

lst1 = Arrays.asList("hi", "admin");
lst2 = Arrays.asList("hI", "hi", "hi");
System.out.println(totalMatch(lst1, lst2)); // ["hI", "hi", "hi"]

lst1 = Arrays.asList("4");
lst2 = Arrays.asList("1", "2", "3", "4", "5");
System.out.println(totalMatch(lst1, lst2)); // ["4"]

/*
Output:
[]
["hI", "Hi"]
["hi", "admin"]
["hI", "hi", "hi"]
["4"]
*/

The output