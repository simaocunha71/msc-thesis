        List<Integer> ll = l.stream().sorted().collect(Collectors.toList());
        int n = ll.size();
        if (n == 0) {
            throw new RuntimeException("List is empty");
        }

        // First element
        if (n == 1) {
            return ll.get(0);
        }

        // Last element
        if (n == 2) {
            return (ll.get(0) + ll.get(1)) / 2.0;
        }

        // Middle element
        if (n % 2 == 0) {
            return (double) (ll.get(n/2-1) + ll.get(n/2)) / 2.0;
        }

        // Middle element
        return (double) ll.get(n/2);
    }
}
