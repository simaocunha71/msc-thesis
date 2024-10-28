        double aDouble = (a instanceof Double) ? (double) a : Double.parseDouble(a.toString().replace(',', '.'));
        double bDouble = (b instanceof Double) ? (double) b : Double.parseDouble(b.toString().replace(',', '.'));

        if (aDouble > bDouble) return Optional.of(a);
        if (aDouble < bDouble) return Optional.of(b);
        return Optional.empty();
    }
}

