        int result = 0;
        int index = 0;
        while (index < lst.size()) {
            if (lst.get(index) % 2 == 0 && index % 2 == 0) {
                result += lst.get(index);
            }
            index += 1;
        }
        return result;
    }
}

