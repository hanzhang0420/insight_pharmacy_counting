# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [My code](README.md#My-code)
4. [Output](README.md#output)



# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

# Input Dataset
The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# My Code
1) Understanding of the Input Dataset:
Counting and Summation problem based on the drug name. 
Count: Individual Prescriber has Unique ID (numetric string), which is used to count the total num of UNIQUE individuals instead of using the precriber's first and last name. 

Summation: Sum over the drug total cost. Data precision problem (check if it is int or floating number). 

2) /src/pharmacy_counting.py
The code is at /src/pharmacy_counting.py. It is a python3 (import sys and re) code and use data structures list, tuples, and dictonary. I used set function in python to find the unique values in a list. 
To run the code, use python3 pharmacy_counting.py input_file_directory output_file_directory (in run.sh).  
The input and output files have to be given in the command line. 


# Output 

Your program needs to create the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file should contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

The code has passed the simple test_1. 


## Repo directory structure

The directory structure for my repo look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── 
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
                    └── top_cost_drug.txt
          
