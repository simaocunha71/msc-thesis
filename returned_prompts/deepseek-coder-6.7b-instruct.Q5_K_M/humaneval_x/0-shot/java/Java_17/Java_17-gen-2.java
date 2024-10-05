        List<Integer> result = new ArrayList<>();
        String[] notes = string.split(" ");

        for (String note : notes) {
            switch (note) {
                case "o":
                    result.add(4);
                    break;
                case "o|":
                    result.add(2);
                    break;
                case ".|":
                    result.add(1);
                    break;
            }
        }

        return result;
    }
}

This code will parse the string and return the number of beats each note lasts. It splits the string into an array of notes, then for each note it checks what it is and adds the corresponding number of beats to the result list.
    */
}

//src/main/java/com/codecool/music/MusicApplication.java
package com.codecool.music;

import com.codecool.music.solution.Solution;

public class MusicApplication {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.parseMusic("o o| 。| o| o| 。| 。| 。| 。| o o"));
    }
}

//src/test/java/com/codecool/music/MusicApplicationTest.java
package com.codecool.music;

import com.codecool.music.solution.Solution;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class MusicApplicationTest {
    Solution solution = new Solution();

    @Test
    void parseMusicTest1() {
        List<Integer> expected = Arrays.asList(4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4);
        assertEquals(expected, solution.parseMusic("o o| .| o| o| .| .| .| .| o o"));
    }

    @Test
    void parseMusicTest2() {