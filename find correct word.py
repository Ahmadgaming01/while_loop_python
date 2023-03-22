password = "Ahmad"
word = ""
count = 0
limit = 3

while word != password:

    if count < limit:

        word = input("Enter password : ")

        count += 1

    elif count == limit:
        print("Your try is finish")
        break
    if word == password:
        print("correct !")
        break