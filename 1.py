try:
    file = open("sample.txt", "r")
    for line in file:
        print(line)
    file.close()
except:
    print("The file 'sample.txt' does not exist.")
