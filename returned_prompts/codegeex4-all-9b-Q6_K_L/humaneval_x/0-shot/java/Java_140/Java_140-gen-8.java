import java.util.*;
import java.lang.*;

class Solution {
    public String fixSpaces(String text) {
        return text.replace("  ", "-").replace(" ", "_");
    }
}