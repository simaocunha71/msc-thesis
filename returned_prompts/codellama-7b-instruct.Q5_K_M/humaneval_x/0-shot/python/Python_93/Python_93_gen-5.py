
def encode(message):
    message = message.replace("a", "z").replace("e", "y").replace("i", "x").replace("o", "w").replace("u", "v").replace("A", "Z").replace("E", "Y").replace("I", "X").replace("O", "W").replace("U", "V")
    message = message.swapcase()
    return message