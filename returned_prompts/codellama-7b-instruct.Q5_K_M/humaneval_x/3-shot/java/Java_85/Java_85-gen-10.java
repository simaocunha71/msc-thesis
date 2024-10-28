        int result = 0;

        for (int i = 1; i < lst.size(); i += 2) {
            result += lst.get(i);
        }
        return result;
    }
}

