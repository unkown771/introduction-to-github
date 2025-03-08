# Author : Smit Desai
# Date: 03-06-2024
# Description: This program is prompt the user to create a txt of some random number file which can
# read by the program and give the average of that every number.


def main():
    with open("numbers.txt","r") as file:
        number1 = 0
        count= 0

        for line in file:
            line = line.strip()
            print(line)


            number1 += int(line)
            count += 1

        if count > 0:
            average = number1/count
            print(f"average: {average:.2f}")
        else:
            print("No number found in the file.")

            """
                Reads a file containing numbers, calculates the sum, and computes the average of the numbers.

                This function opens a file named 'numbers.txt', processes each line to extract integer values, 
                and calculates both the sum and the average of the numbers. It also handles invalid data by 
                skipping lines that do not contain valid integers.

            """

if __name__ == "__main__":
    main()


