        String [] arr = {"txt", "exe", "dll"};
        if(file_name.length() > 3){
            return "No";
        }
        if(file_name.length() == 0){
            return "No";
        }
        if(file_name.length() == 1){
            return "No";
        }
        if(file_name.length() == 2 && !file_name.contains(".")){
            return "No";
        }
        String [] arr1 = file_name.split("\\.");
        if(arr1.length != 2){
            return "No";
        }
        if(Character.isDigit(arr1[0].charAt(0))){
            return "No";
        }
        if(file_name.charAt(file_name.length() - 1) == '.'){
            return "No";
        }
        for(int i = 0; i < arr.length; i++){
            if(arr[i].equals(arr1[1])){
                return "Yes";
            }
        }
        return "No";
    }
}











































































































































































































































