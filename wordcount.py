text = input("Text:")
count=1
for char in text:
	if char == " ":
		count+=1
print("Words: %d" %count)