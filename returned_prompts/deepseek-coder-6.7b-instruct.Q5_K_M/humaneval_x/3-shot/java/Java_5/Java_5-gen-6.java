        List<Integer> result = new ArrayList<>();

        if (!numbers.isEmpty()) {
            result.add(numbers.get(0));

            for (int i = 1; i < numbers.size(); i++) {
                result.add(delimiter);
                result.add(numbers.get(i));
            }
        }

        return result;
     }
}

