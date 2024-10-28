
class_name = "Slices";
extensions = ["SErviNGSliCes", "Cheese", "StuFfed"];

        List<String> extensionsList = new ArrayList<>();
        for (String str: extensions) {
            int cap = 0;
            int sm = 0;
            for (int i = 0; i < str.length(); i++) {
                if (Character.isUpperCase(str.charAt(i))) {
                    cap++;
                } else {
                    sm++;
                }
            }
            double strength = (double)cap - (double)sm;
            extensionsList.add(strength+" - "+str);
        }
        int maxStrengthIndex = 0;
        double maxStrength = Integer.MIN_VALUE;
        for (int i = 0; i < extensionsList.size(); i++) {
            if (Double.parseDouble(extensionsList.get(i).substring(0, extensionsList.get(i).indexOf(" - "))) > maxStrength) {
                maxStrength = Double.parseDouble(extensionsList.get(i).substring(0, extensionsList.get(i).indexOf(" - ")));
                maxStrengthIndex = i;
            }
        }
        String strongestExtension = class_name+"."+extensions.get(maxStrengthIndex);
        return strongestExtension;
    }
}















































































































































































