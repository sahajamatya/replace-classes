# Sahaj Amatya, 1001661825
import sys

# Returns the file line as a list


def listifyLines(line):
    arr = line.split(" ")
    while("" in arr):
        arr.remove("")
    arr[len(arr) - 1] = arr[len(arr) - 1].replace('\n', '')
    return arr

# Returns the file data as a 2D list


def getFileData(fileName):
    inputFile = open(fileName, 'r')
    lines = inputFile.readlines()
    fileData = []
    for line in lines:
        fileData.append(listifyLines(line))
    inputFile.close()
    return fileData

# Returns a sorted list of all unique classes in the file


def getClasses(fileName):
    inputFile = open(fileName, 'r')
    lines = inputFile.readlines()
    classes = []
    for line in lines:
        line = listifyLines(line)
        if int(line[len(line) - 1]) not in classes:
            classes.append(int(line[len(line) - 1]))
    inputFile.close()
    return sorted(classes)

# Writes out a file with the specified substitutions


def generateOutputFile(fileData, fileName):
    outputFile = open(fileName, 'a')
    num = len(fileData[0][0]) + 4
    for data in fileData:
        counter = 0
        tempString = ""
        while(counter < len(data)):
            tempString += data[counter].ljust(num) + " "
            counter += 1
        tempString += "\n"
        outputFile.write(tempString)
    outputFile.close()


def main():
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    fileData = getFileData(inputFileName)
    classes = getClasses(inputFileName)

    print("\nThese are all the unique classes in this dataset:", classes)
    print("\n")

    substitutions = {}

    for c in classes:
        substitutions[c] = input(
            "Enter string substitution for class %d: " % c)
    print("\n")

    for data in fileData:
        data[len(data) - 1] = substitutions[int(data[len(data) - 1])]

    print("Generating output file...\n")
    generateOutputFile(fileData, outputFileName)
    print("Output file %s generated successfully." % outputFileName)


if __name__ == "__main__":
    main()
