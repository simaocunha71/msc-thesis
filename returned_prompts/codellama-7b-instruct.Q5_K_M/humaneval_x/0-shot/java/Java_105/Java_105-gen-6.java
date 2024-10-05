        if (arr.length === 0) {
            return [];
        }

        let result = arr.sort((a, b) => {
            return a - b;
        });

        result = result.reverse();

        let string = result.map((val) => {
            if (val < 1 || val > 9) {
                return "";
            } else {
                return val;
            }
        });

        let stringLength = [];
        for (let i = 0; i < string.length; i++) {
            stringLength[i] = string[i].toString().length;
        }

        let length = Math.max.apply(null, stringLength);

        for (let i = 0; i < string.length; i++) {
            string[i] = string[i].toString();
            if (string[i].length < length) {
                string[i] = string[i].padStart(length, "0");
            }
        }

        let words = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ];

        let returnArr = [];
        for (let i = 0; i < string.length; i++) {
            returnArr[i] = words[string[i]];
        }

        return returnArr;
    }
}

