import re
from decimal import Decimal

def getFileContents():
    # Open the file for reading
    with open('simulation-results/throughputipc.txt', 'r') as file:
        # read the contents of the file
        file_content = file.read()

        # use regular expression to search for throughput ipc in the file content
        matches = re.findall(r'\d*\.?\d+', file_content)
        if len(matches) >= 8:
            # extract the matched number
            number1 = Decimal(matches[0])
            number2 = Decimal(matches[1])
            number3 = Decimal(matches[2])
            number4 = Decimal(matches[3])
            number5 = Decimal(matches[4])
            number6 = Decimal(matches[5])
            number7 = Decimal(matches[6])
            number8 = Decimal(matches[7])
            # perform calculations with the extracted number
            percentImprovement1 = ((number5 - number1) / number1) * 100
            percentImprovement2 = ((number6 - number2) / number2) * 100
            percentImprovement3 = ((number7 - number3) / number3) * 100
            percentImprovement4 = ((number8 - number4) / number4) * 100
            
            # Print the result
            print(f"% Improvement(1): {percentImprovement1}%")
            print(f"% Improvement(2): {percentImprovement2}%")
            print(f"% Improvement(3): {percentImprovement3}%")
            print(f"% Improvement(4): {percentImprovement4}%")
        else:
            print("No Number found in the file.")


if __name__ == "__main__":
    getFileContents()