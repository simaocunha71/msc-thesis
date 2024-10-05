    List<Integer> result = new ArrayList<>();

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            result.add(i);
        } else {
            result.add(i + 1);
        }
    }

    return result;
    }
}


# Python

def makeAPile(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(i)
        else:
            result.append(i + 1)
    return result


if __name__ == "__main__":
    print(makeAPile(3))


# Python


def makeAPile(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(i)
        else:
            result.append(i + 1)
    return result


if __name__ == "__main__":
    print(makeAPile(3))


















































































































































































































































