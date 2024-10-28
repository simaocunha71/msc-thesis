        List<Optional<Integer>> result = new ArrayList<>();

        Optional<Integer> max = lst.stream()
                .filter(n -> n < 0)
                .max(Integer::compareTo);

        Optional<Integer> min = lst.stream()
                .filter(n -> n > 0)
                .min(Integer::compareTo);

        result.add(max);
        result.add(min);

        return result;
    }
}


A: 
The problem is that it's returning a List of Optional<Integer>, not a tuple. Python has tuples and JavaScript has arrays which can be used to return multiple values, but Java doesn't directly support this.

