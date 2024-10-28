        List<Integer> copy = new ArrayList<>(array);
        int sum = array.get(0) + array.get(array.size() - 1);
        boolean oddSum = sum % 2 == 1;

        Collections.sort(copy, oddSum ? Collections.reverseOrder() : null);

        return copy;
     }
}

