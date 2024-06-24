s = " this is a new word"
print(s)
print(s[2], ",3rd char")
print(s*2, ",print twice")
print(s[0:9], ",until 9th word")
print(s[0:-3], ",remove last 3 char")
print(s[:8], ",until 8")
print(s[3:17:2]) # 3rd position is a step value.
print(s[::-1]) # reverse order.
print(s.strip())
print(s.find("is", 0, 9))
print(s.count("a"))

collection_of_words = """list,
set,
dictionary"""

print(collection_of_words)
