while True:
    print("1.Save 2.View 3.Exit")
    c=input()

    if c=="1":
        site=input("Website: ")
        pwd=input("Password: ")
        with open("passwords.txt","a") as f:
            f.write(site+" : "+pwd+"\n")

    elif c=="2":
        print(open("passwords.txt").read())

    else:
        break
