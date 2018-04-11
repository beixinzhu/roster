# Roster Compatibility Check

## Usage

This is a tool for checking the compatability of Myucla, Piazza and Gradescope.

To download the roster in MyUcla, please go to Class Roster -> Roster Download -> Comma-Separated

To download the roster in Gradescope, please go to Assignments -> Download Grades -> Download CSV

To download the roster in Piazza, please go to Management Enrollment -> Enroll Students -> Student Roster: Download Roster as CSV

To use the tool under default settings, please put all three rosters under the same folder, rename them with myucla.csv, piazza.csv, gradescope.csv respectively. And run:

        python roster.py

You will see a file named result.csv in the same folder.

Usage: 
        
        roster.py [-h] [-m MYUCLA] [-p PIAZZA] [-g GRADESCOPE] [-s SAVE] [--separator SEPARATOR]

Optional arguments:

        -h, --help            show this help message and exit
        -m MYUCLA, --myucla MYUCLA
                        File name of MyUcla roster (default: ./myucla.csv)
        -p PIAZZA, --piazza PIAZZA
                        File name of Piazza roster (default: ./piazza.csv)
        -g GRADESCOPE, --gradescope GRADESCOPE
                        File name of Gradescope roster (default:
                        ./gradescope.csv)
        -s SAVE, --save SAVE  File name of Gradescope roster (default:
                        ./gradescope.csv)
        --separator SEPARATOR
                        The separator of cells in the result csv file
                        (default: comma(,))

Please do NOT change the file layout after downloading.

## Matching Criteria

To match Gradescope and MyUcla roster, we match simply by comparing UID (SID).

To match MyUcla and Piazza roster, since Piazza does not contain UID, we will label "matched" when we found either email or name matched.

To match names, since students may have different format of names registered (e.g first name + second name or inverse, nicknames or preferred names), we label two name "matched" when we found at least two words matched. For example:

        name1 = "David E. Smith"
        name2 = "Smith David"
        name3 = "Smith"

will be labelled as:

        match_names(name1, name2) = True
        match_names(name2, name3) = False

According to this, please double-check with the students listed in result file (especially associated with Piazza roster) before any further actions.

We do NOT check the compatibility between rosters of Gradescope and Piazza.

-------------------
## Apr 10 Update:

Fix the csv file opening problem. You can open the csv file with the separator comma (,), or you can set the separator as the csv browser can recognize. 