        int sum = 0;
        for (int i = 0; i < array.size(); i++) {
            sum += array.get(i);
        }
        if ((sum & 1) == 0) {
            Collections.sort(array);
        } else {
            Collections.sort(array, Collections.reverseOrder());
        }
        return array;

    }
}
