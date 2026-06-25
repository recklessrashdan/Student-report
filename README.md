# Student Report

A simple Python script to calculate and display student mark reports including total marks and average marks.

## Features

- Calculates the **total marks** from multiple subjects
- Calculates the **average marks** across subjects
- Simple command-line interface

## How to Use

1. **Run the script:**
   ```bash
   python "Student Report.py"
   ```

2. **Enter marks when prompted:**
   The script will ask you to enter marks three times:
   ```
   Enter yout 1st mark: 85
   Enter yout 2nd mark: 92
   Enter yout 3rd mark: 78
   ```

3. **View results:**
   After entering all marks, the script will display:
   ```
   Student Mark Report
   Total Marks- 255
   Average Marks- 85.0
   ```

## How to Change the Number of Marks

To modify the script to accept a different number of marks, follow these steps:

### Example: Changing from 3 marks to 5 marks

1. **Add more input lines:**
   Replace the input section with:
   ```python
   marks1=int(input("Enter yout 1st mark: "))
   marks2=int(input("Enter yout 2nd mark: "))
   marks3=int(input("Enter yout 3rd mark: "))
   marks4=int(input("Enter yout 4th mark: "))
   marks5=int(input("Enter yout 5th mark: "))
   ```

2. **Update the total() function:**
   ```python
   def total():
       total2=(marks1+marks2+marks3+marks4+marks5)
       return(total2)
   ```

3. **Update the multiply() function (for average):**
   ```python
   def multiply():
       multiply2=(marks1+marks2+marks3+marks4+marks5)/5
       return(multiply2)
   ```

### General Formula

- **For N marks:**
  - Add N input statements (marks1 through marksN)
  - In `total()`: Add all marks: `marks1+marks2+...+marksN`
  - In `multiply()`: Divide by N: `(marks1+marks2+...+marksN)/N`

## Requirements

- Python 3.x

## Notes

- The script uses `time.sleep()` to add delays for better readability
- Feel free to modify the prompts or add additional calculations as needed
