def main():
    print("Hello, World!!!!")

    file = open("starter.log", "r")
    reviewLines = file.readlines()
    file.close()

    for line in reviewLines:
        clean = line.strip()
        print(clean)

if __name__ == "__main__":
    main()
