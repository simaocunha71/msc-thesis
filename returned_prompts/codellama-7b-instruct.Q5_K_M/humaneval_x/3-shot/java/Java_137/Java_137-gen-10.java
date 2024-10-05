        if (a instanceof Float || a instanceof Double) {
            if ((Double) a > (Double) b) return Optional.of(a);
            else if ((Double) a < (Double) b) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof Integer || a instanceof Long) {
            if ((Long) a > (Long) b) return Optional.of(a);
            else if ((Long) a < (Long) b) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof String) {
            String as = (String) a;
            String bs = (String) b;

            String[] as_comps = as.split(",");
            String[] bs_comps = bs.split(",");

            if (as_comps.length == 1 && bs_comps.length == 1) {
                double da = Double.parseDouble(as);
                double db = Double.parseDouble(bs);

                if (da > db) return Optional.of(a);
                else if (da < db) return Optional.of(b);
                else return Optional.empty();
            } else if (as_comps.length == 1 && bs_comps.length == 2) {
                double da = Double.parseDouble(as);
                double db = Double.parseDouble(bs_comps[0]);
                double dc = Double.parseDouble(bs_comps[1]);

                if (da > db) {
                    if (da > dc) return Optional.of(a);
                    else return Optional.of(b);
                } else {
                    if (db > dc) return Optional.of(b);
                    else return Optional.of(a);
                }
            } else if (as_comps.length == 2 && bs_comps.length == 1) {
                double da = Double.parseDouble(as_comps[0]);
                double db = Double.parseDouble(as_comps[1]);
                double dc = Double.parseDouble(bs);

                if (da > db) {
                    if (