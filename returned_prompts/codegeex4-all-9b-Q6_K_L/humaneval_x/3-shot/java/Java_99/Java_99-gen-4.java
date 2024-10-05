
The first two problems are correct.
The third problem is also correct, but the method name should be truncateNumber, not countUpper. countUpper seems to be a misnomer.
The fourth problem is wrong. You should be rounding towards zero, not away from it. So, closest_integer("14.5") should return 14, and closest_integer("-14.5") should return -14.