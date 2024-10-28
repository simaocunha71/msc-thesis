        int result = 0;
        int index = 1;
        for (int i = 0; i < lst.size(); i++) {
            if (index % 2 == 0 && lst.get(i) % 2 != 0) {
                result += lst.get(i);
            }
            index += 1;
        }
        return result;
    }
}

