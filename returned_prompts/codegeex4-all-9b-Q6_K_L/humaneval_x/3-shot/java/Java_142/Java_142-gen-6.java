        int result = 0;

        for (int i = 0; i < lst.size(); i++) {
            int square = 1;
            int cube = 1;

            if (i % 3 == 0) square = lst.get(i) * lst.get(i);
            if (i % 4 == 0 && i % 3 != 0) cube = lst.get(i) * lst.get(i) * lst.get(i);

            result += square + cube;
        }

        return result;
    }
}

