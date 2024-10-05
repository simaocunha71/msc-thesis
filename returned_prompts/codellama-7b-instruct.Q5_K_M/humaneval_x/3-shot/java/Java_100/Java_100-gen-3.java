        List<Integer> result = new ArrayList<>();
        while (n > 0) {
            result.add(n);
            if (n % 2 == 0) n += 1;
            else n += 2;
        }
        return result;
    }
}

