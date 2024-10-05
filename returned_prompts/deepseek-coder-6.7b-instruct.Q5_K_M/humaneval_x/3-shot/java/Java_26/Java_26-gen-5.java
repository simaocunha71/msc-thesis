        return numbers.stream()
                .distinct()
                .collect(Collectors.toList());
     }
 }

