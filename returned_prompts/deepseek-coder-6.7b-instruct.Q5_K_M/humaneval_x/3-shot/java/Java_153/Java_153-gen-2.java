        String strongest_extension = extensions.get(0);
        double max_strength = strength(extensions.get(0));

        for (String extension  : extensions)  {
            double strength_of_extension = strength(extension);
            if  (strength_of_extension > max_strength)  {
                max_strength = strength_of_extension;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }

    private double strength(String extension)  {
        int upper = 0;
        int lower = 0;
        for  (char c  : extension.toCharArray())  {
            if  (Character.isUpperCase(c)) upper += 1;
            if  (Character.isLowerCase(c)) lower += 1;
        }
        return (double)upper - (double)lower;
    }
}

