        if (extensions.isEmpty()) return "";

        // calculate strengths and sort
        List<Double> strengths = new ArrayList<>();
        for (String ext : extensions) {
            int cap = 0;
            int sm = 0;
            for (int i = 0; i < ext.length(); i++) {
                if (ext.charAt(i) >= 'A' && ext.charAt(i) <= 'Z') cap++;
                else sm++;
            }
            strengths.add(-1.0 * (double) cap / sm);
        }
        Collections.sort(strengths);

        // find strongest extension
        double strongest_strength = strengths.get(strengths.size() - 1);
        int strongest_idx = -1;
        for (int i = 0; i < strengths.size(); i++) {
            if (strengths.get(i) == strongest_strength) {
                strongest_idx = i;
                break;
            }
        }

        // return class name with strongest extension
        return class_name + "." + extensions.get(strongest_idx);
    }
}

