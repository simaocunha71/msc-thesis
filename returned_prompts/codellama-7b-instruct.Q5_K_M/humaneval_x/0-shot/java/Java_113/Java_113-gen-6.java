        for (String i: lst) {
            int count = 0;
            for (char j: i.toCharArray()) {
                if (Character.getNumericValue(j) % 2 == 1) {
                    count++;
                }
            }
            lst.set(i, "the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.");
        }
        return lst;
    }
}
