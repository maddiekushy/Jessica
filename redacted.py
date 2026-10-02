target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]

classified = input("Enter a sentence: ")

words =classified.split()

redacted = []
for word in words:
     if word in target_words:
        replaced = word.replace(word, "REDACTED")
        redacted.append(replaced)
    else:
        redacted.append(word)

message = " ".join(redacted)
print("Message:")
print(message)
