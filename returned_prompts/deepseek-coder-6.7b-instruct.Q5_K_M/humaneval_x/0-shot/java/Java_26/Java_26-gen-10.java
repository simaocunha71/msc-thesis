        Map<Integer, Long> counts = numbers.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        List<Integer> result = numbers.stream()
                .filter(n -> counts.get(n) == 1)
                .collect(Collectors.toList());

        return result;
    }
}

Explanation:
The solution first counts the occurrences of each number in the list. Then it filters the list to only include numbers that occur exactly once. 

*/

