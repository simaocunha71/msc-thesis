    public String sortNumbers(String numbers) {
        // Convert the input string into an array of strings, splitting by space
        String[] arr = numbers.split(" ");
        
        // Create an array list to store the string values
        ArrayList<String> list = new ArrayList<String>();
        
        // Loop through the array and add the string values to the list
        for (String str : arr) {
            list.add(str);
        }
        
        // Sort the list using the Collections.sort() method
        Collections.sort(list);
        
        // Initialize an empty string to store the sorted result
        String result = "";
        
        // Loop through the sorted list and concatenate the string values
        for (String str : list) {
            result += str + " ";
        }
        
        // Remove the trailing space and return the sorted result
        return result.trim();
    } 
}
