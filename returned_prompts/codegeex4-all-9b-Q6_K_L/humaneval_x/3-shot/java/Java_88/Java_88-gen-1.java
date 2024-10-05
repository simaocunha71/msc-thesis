        List<Integer> result = new ArrayList<>(array);
        result.sort((a, b) -> {
            if ((a + b) % 2 == 0) return b.compareTo(a);
            else return a.compareTo(b);
        });
        return result;
    }
}

