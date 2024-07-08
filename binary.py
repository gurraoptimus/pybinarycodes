message = "BinaryCodes"
Binary = " ".join(format(ord(c), "b") for c in message)

print(Binary)