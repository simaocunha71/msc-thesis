    return {key: value for key, value in dict.fromkeys(test.split()).items() if test.count(key) > 1}

