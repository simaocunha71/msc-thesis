        String[] number_array = numbers.split(" ");
        Arrays.sort(number_array, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return Integer.parseInt(s1) - Integer.parseInt(s2);
            }
        });
        return String.join(" ", number_array);
    }
}

