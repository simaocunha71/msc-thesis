        Collections.sort(l);
        int length = l.size();

        if (length % 2 == 0) {
            int middle_index = length / 2;
            return (l.get(middle_index) + l.get(middle_index - 1)) / 2.0;
        } else {
            return l.get(length / 2);
        }
    }
}




```