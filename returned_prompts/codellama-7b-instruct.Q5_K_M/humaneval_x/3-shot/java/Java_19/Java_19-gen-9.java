        String[] number_array = numbers.split(" ");
        Arrays.sort(number_array, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return Integer.valueOf(a).compareTo(Integer.valueOf(b));
            }
        });
        return String.join(" ", number_array);
    }
}

