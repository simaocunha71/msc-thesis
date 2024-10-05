        int maxStrength = Integer.MIN_VALUE;
        String strongestExtension = "";

        for(String extension : extensions){
            int strength = countUpperCase(extension) - countLowerCase(extension);
            if(strength > maxStrength){
                maxStrength = strength;
                strongestExtension = extension;
            }
        }

        return class_name + "." + strongestExtension;
    }

    private int countUpperCase(String str){
        int count = 0;
        for(char c : str.toCharArray()){
            if(Character.isUpperCase(c)){
                count++;
            }
        }
        return count;
    }

    private int countLowerCase(String str){
        int count = 0;
        for(char c : str.toCharArray()){
            if(Character.isLowerCase(c)){
                count++;
            }
        }
        return count;
    }
}

