        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";

        for  (String ext : extensions) {
            int strength = 0;
            for  (char c : ext.toCharArray()) {
                if  (Character.isUpperCase(c)) strength++;
                else if  (Character.isLowerCase(c)) strength--;
             }

            if  (strength > max_strength) {
                max_strength = strength;
                strongest_extension = ext;
             }
         }

        return class_name + "." + strongest_extension;
     }
}

