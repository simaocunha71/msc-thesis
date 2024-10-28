        if (arr.size() == 0)
            return true;

        int index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > arr.get((i + 1) % arr.size())) {
                if (index != 0)
                    return false;
                index = i;
            }
        }

        return (index == 0) || ((index + 1) % arr.size() == 0);
    }
}

