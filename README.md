# Roster Compatibility Check

This is a tool for checking the compatability of Myucla, Piazza and Gradescope.

To download the roster in MyUcla, please go to Class Roster -> Roster Download -> Comma-Separated

To download the roster in Gradescope, please go to Assignments -> Download Grades -> Download CSV

To download the roster in Piazza, please go to Management Enrollment -> Enroll Students -> Student Roster: Download Roster as CSV

To use the tool under default settings, please put all three rosters under the same folder, rename them with myucla.csv, piazza.csv, gradescope.csv respectively. And run:

        python roster.py

You will see a file named result.csv in the same folder.

To set the directory of read-in file and output file, please run:

        python roster.py -m PATHOF_MYUCLA_ROSTER.CSV -p PATHOF_PIAZZA_ROSTER.CSV -g PATHOF_GRADESCOPE_ROSTER.csv -s PATHOF_SAVE.CSV

or

        python roster.py --myucla PATHOF_MYUCLA_ROSTER.CSV --piazza PATHOF_PIAZZA_ROSTER.CSV --gradescope PATHOF_GRADESCOPE_ROSTER.csv --save PATHOF_SAVE.CSV

Please do NOT change the file layout after downloading.