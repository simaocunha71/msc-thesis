        Optional<Integer> max = lst.stream()
 .filter(i -> i < 0)
 .max(Integer::compareTo);

        Optional<Integer> min = lst.stream()
 .filter(i -> i > 0)
 .min(Integer::compareTo);

        return Arrays.asList(max, min);
     }
}

