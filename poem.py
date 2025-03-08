# Author : Smit Desai
# Date: 03-07-2024
# Description: This program is prompt the user to create a txt file of poem which can read and write by
# the program and give that poem as output.

import os


file_name = input("Please enter the name of the file you want to read and summarize: ")

while not os.path.exists(file_name):
    print(f"The file '{file_name}' does not exist. Please try again.")
    file_name = input("Please enter the name of the file you want to read and summarize: ")

poem_title = ""
poem_author = ""
poem_lines = []

with open(file_name, 'r') as file:
    poem_title = file.readline().strip()
    poem_author = file.readline().strip()

    poem_lines = [line.strip() for line in file.readlines()]

with open("Output.txt", 'w') as output_file:
    output_file.write(f"Poem Title: {poem_title}\n")
    output_file.write(f"Poem Author: {poem_author}\n")
    output_file.write(f"Number of Lines: {len(poem_lines)}\n")
    output_file.write("\nFirst Three Lines of the Poem:\n")


    for i in range(min(3, len(poem_lines))):
        output_file.write(f"{poem_lines[i]}\n")
print(f"The summary of the poem has been written to 'Output.txt'.")
"""
Reads a poem file and summarizes its content.

This script prompts the user for the name of a file containing a poem, reads the title, 
author, and lines of the poem, and generates a summary. The summary includes the poem's 
title, author, the number of lines, and the first three lines of the poem. The summary 
is then written to a new file called 'Output.txt'.

"""









