def main():
    print("Hello, World!!!!")

    LINE_Count = 0
    INFO_Count = 0
    WARN_Count = 0
    ERROR_Count = 0


    file = open("starter.log", "r")
    reviewLines = file.readlines()
    

    for line in reviewLines:
        clean = line.strip()

        LINE_Count += 1
        if "INFO" in clean:
            INFO_Count += 1
        if "WARN" in clean:
            WARN_Count += 1
        if "ERROR" in clean:
            ERROR_Count += 1

    if ERROR_Count > 5:
         print("WARNING: Too many errors in the log")
        
        
    file.close()    


    print("Log Summary:")
    print("--------------")
    print("Total Lines: " ,LINE_Count)
    print("INFO: " ,INFO_Count)
    print("WARN: " ,WARN_Count)
    print("ERROR: " ,ERROR_Count)

    


if __name__ == "__main__":
    main()
