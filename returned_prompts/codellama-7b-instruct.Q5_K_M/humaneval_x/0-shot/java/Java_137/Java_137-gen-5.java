        if(a instanceof Number && b instanceof Number) {
            Number aNum = (Number)a;
            Number bNum = (Number)b;
            if(aNum.doubleValue() > bNum.doubleValue()) {
                return Optional.of(a);
            } else if(aNum.doubleValue() < bNum.doubleValue()) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        }
        if(a instanceof String && b instanceof String) {
            String aStr = (String)a;
            String bStr = (String)b;
            if(aStr.equals(bStr)) {
                return Optional.empty();
            }
            String[] aSplit = aStr.split(",");
            String[] bSplit = bStr.split(",");
            if(aSplit.length == 2 && bSplit.length == 2) {
                double aVal = Double.parseDouble(aSplit[0])+Double.parseDouble(aSplit[1])/100;
                double bVal = Double.parseDouble(bSplit[0])+Double.parseDouble(bSplit[1])/100;
                if(aVal > bVal) {
                    return Optional.of(a);
                } else if(aVal < bVal) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            } else {
                double aVal = Double.parseDouble(aStr);
                double bVal = Double.parseDouble(bStr);
                if(aVal > bVal) {
                    return Optional.of(a);
                } else if(aVal < bVal) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            }
        }
        throw new IllegalArgumentException("Invalid input");
    }
}
