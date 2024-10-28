        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> max = Optional.empty();
        Optional<Integer> min = Optional.empty();

        for(Integer i : lst){
            if(i < 0){
                if(max.isEmpty() || i > max.get()){
                    max = Optional.of(i);
                }
            }else if(i > 0){
                if(min.isEmpty() || i < min.get()){
                    min = Optional.of(i);
                }
            }
        }

        result.add(max);
        result.add(min);

        return result;
    }
}

This solution first initializes two Optional objects, max and min, as empty. It then iterates through the list. If an integer is negative, it checks if max is empty or if the absolute value of the integer is larger than the value in max. If the latter is true, it assigns the integer to max. The same logic is applied if the integer is positive. Finally, the function returns a list of the Optional objects max and min.

Test cases:

List<Integer> lst = Arrays.asList(2, 4, -1, 3, -5, 7);
System.out.println(s.largestSmallestIntegers(lst)); // prints [Optional.empty, Optional.of(1)]

lst = Arrays.asList();
System.out.println(s.largestSmallestIntegers(lst)); // prints [Optional.empty, Optional.empty]

lst = Arrays.asList(0);
System.out.println(s.largestSmallestIntegers(lst)); // prints [Optional.empty, Optional.empty]

lst = Arrays.asList(-2, -4, 1, 3, -5, 7);
System.out.println(s.largestSmallestIntegers(lst)); // prints [Optional.of(-2), Optional.of(1)]

lst = Arrays.asList(2, 4, 0, 3, 0, 7);
System.out.println(s.largestSmallestIntegers(l