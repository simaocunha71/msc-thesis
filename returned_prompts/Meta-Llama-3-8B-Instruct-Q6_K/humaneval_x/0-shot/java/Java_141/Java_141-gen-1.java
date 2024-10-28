Here is a Java solution for the problem:

```java
public String filenameCheck(String file_name) {
    String[] validExtensions = {"txt", "exe", "dll"};

    // Check if the file name contains a dot
    if (!file_name.contains(".")) {
        return "No";
    }

    // Split the file name into two parts
    String[] parts = file_name.split("\\.");

    // Check if the file name contains more than three digits
    if (parts[0].matches("\\d{4,}")) {
        return "No";
    }

    // Check if the file name starts with a letter from the latin alphabet
    if (!parts[0].matches("^[a-zA-Z].*")) {
        return "No";
    }

    // Check if the file name's extension is valid
    if (!Arrays.asList(validExtensions).contains(parts[1].trim())) {
        return "No";
    }

    return "Yes";
}
```
This function first checks if the file name contains a dot. If it does not, it returns "No". Then it splits the file name into two parts and checks if the first part contains more than three digits. If it does, it returns "No". Then it checks if the first part starts with a letter from the latin alphabet. If it does not, it returns "No". Finally, it checks if the file name's extension is valid. If it is not, it returns "No". If all the conditions are met, it returns "Yes".