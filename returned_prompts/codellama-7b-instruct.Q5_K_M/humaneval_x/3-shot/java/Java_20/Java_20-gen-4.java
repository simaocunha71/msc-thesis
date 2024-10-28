        List<Double> result = new ArrayList<>();

        Collections.sort(numbers);

        int index_smaller = numbers.indexOf(numbers.get(0));
        int index_larger = numbers.indexOf(numbers.get(numbers.size() - 1));

        if (index_smaller == index_larger) {
            result.add(numbers.get(index_smaller));
            result.add(numbers.get(index_larger));
            return result;
        }

        for (int i = 1; i < numbers.size(); i++) {
            if (index_larger - index_smaller == 1) {
                result.add(numbers.get(index_smaller));
                result.add(numbers.get(index_larger));
                return result;
            }
            if (index_smaller + i == index_larger) {
                result.add(numbers.get(index_smaller));
                result.add(numbers.get(index_larger));
                return result;
            }
            if (numbers.get(index_smaller + i) - numbers.get(index_smaller) ==
                    numbers.get(index_larger) - numbers.get(index_larger + i)) {
                result.add(numbers.get(index_smaller + i));
                result.add(numbers.get(index_larger + i));
                return result;
            }
            if (numbers.get(index_smaller + i) - numbers.get(index_smaller) >
                    numbers.get(index_larger) - numbers.get(index_larger + i)) {
                index_larger += i;
            } else {
                index_smaller += i;
            }
        }
        return result;
    }
}

