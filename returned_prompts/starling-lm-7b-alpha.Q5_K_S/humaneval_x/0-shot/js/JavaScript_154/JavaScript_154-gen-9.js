let result = false;

for(let i = 0; i < a.length; i++) {
    const subString = a.substring(i);
    if (subString.includes(b)) {
        result = true;
        break A;
    }
}

for(let i = 0; i < b.length; i++) {
    const rotatedString = b.slice(i) + b.slice(0,i);
    for(let j = 0; j < a.length; j++) {
        const subString = a.substring(j);
        if (subString.includes(rotatedString)) {
            result = true;
            break A;
        }
    }
}

return result;
};

cycpatternCheck("abcd","abd");  // Expected: false
cycpatternCheck("hello","ell"); // Expected: true
cycpatternCheck("whassup","psus"); // Expected: false
cycpatternCheck("abab","baa"); // Expected: true
cycpatternCheck("efef","eeff"); // Expected: false
cycpatternCheck("himenss","simen"); // Expected: true







































































































































































































































