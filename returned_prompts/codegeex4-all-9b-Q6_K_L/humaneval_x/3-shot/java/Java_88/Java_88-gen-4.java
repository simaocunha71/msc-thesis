        List<Integer> copy = new ArrayList<>(array);

        int sum = copy.get(0) + copy.get(copy.size() - 1);
        if (sum % 2 == 0) Collections.sort(copy, Collections.reverseOrder());
        else Collections.sort(copy);

        return copy;
    }
}

