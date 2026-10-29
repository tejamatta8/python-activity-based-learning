text = input("Enter a string: ")

if len(text) == 0:
    print("Empty string")
else:
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    print("Original String:", text)
    print("Compressed String:", compressed)
    print("Original Length:", len(text))
    print("Compressed Length:", len(compressed))
