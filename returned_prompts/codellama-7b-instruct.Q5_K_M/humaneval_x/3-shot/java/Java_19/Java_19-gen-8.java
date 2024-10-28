        String[] tokens = numbers.split(" ");
        Arrays.sort(tokens, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return a.compareTo(b);
            }
        });
        return String.join(" ", tokens);
    }
}

