from pathlib import Path

class LogAnalyzer:

    def __init__(self, fileName):
       self.LINE_Count = 0
       self.INFO_Count = 0
       self.WARN_Count = 0
       self.ERROR_Count = 0
       self.reviewLines = []
       self.fileName = fileName

    def analyze_logs(self):
        print("Hello, World!!!!")
        file = open(self.fileName, "r")
        reviewLines = file.readlines()
    

        for line in reviewLines:
            clean = line.strip()
            self.LINE_Count += 1
            if "INFO" in clean:
                self.INFO_Count += 1
            if "WARN" in clean:
                self.WARN_Count += 1
            if "ERROR" in clean:
                self.ERROR_Count += 1

        if self.ERROR_Count > 5:
         print("WARNING: Too many errors in the log")
        
        
        file.close()    

    def print_summary(self):
      print("Log Summary:")
      print("--------------")
      print("Total Lines: " ,self.LINE_Count)
      print("INFO: " ,self.INFO_Count)
      print("WARN: " ,self.WARN_Count)
      print("ERROR: " ,self.ERROR_Count)

def main():

    while not fileCheck.is_file():

        fileName = input("Enter the log file name: ")
        fileCheck = Path(fileName)

        if fileCheck.is_file():
            print("Successfully opened file:")

            analyzer = LogAnalyzer(fileName)
            analyzer.analyze_logs()
            analyzer.print_summary()
        else: 
            print("Error: File does not exist, please try again.")
             
    analyzer = LogAnalyzer(fileName)
    analyzer.analyze_logs()
    analyzer.print_summary()           
    


if __name__ == "__main__":
   main()


