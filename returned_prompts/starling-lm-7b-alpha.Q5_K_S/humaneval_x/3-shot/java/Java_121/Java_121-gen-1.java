        int result = 0;
        int index = 0;
        while (index < lst.size()) {
            if (lst.get(index) % 2 == 0) {
                index++;
                continue;
            }
            result += lst.get(index);
            index += 2;
        }
        return result;
    }
}

