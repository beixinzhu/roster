import argparse
import pdb
import csv

parser = argparse.ArgumentParser(description='Roster Compatability of MyUcla, Gradescope and Piazza')
parser.add_argument('-m', '--myucla', default='./myucla.csv', type=str,\
                    help='File name of MyUcla roster (default: ./myucla.csv)')
parser.add_argument('-p', '--piazza', default='./piazza.csv', type=str,\
                    help='File name of Piazza roster (default: ./piazza.csv)')
parser.add_argument('-g', '--gradescope', default='./gradescope.csv', type=str,\
                    help='File name of Gradescope roster (default: ./gradescope.csv)')
parser.add_argument('-s', '--save', default='./result.csv', type=str,\
                    help='File name of Gradescope roster (default: ./gradescope.csv)')
parser.add_argument('--separator', default = ',', type = str,\
                    help = 'The separator of cells in the result csv file (default: comma(,))')

def match_names(n1,n2):
    name1 = n1.replace(',','')
    name2 = n2.replace(',','')
    name1 = set(name1.lower().split(' '))
    name2 = set(name2.lower().split(' '))
    
    if len(name1.intersection(name2)) >= 2:
        return True
    return False

def read1(filename, name,email,uid):
    print "Reading roster " + filename
    name_idx, email_idx, uid_idx = -1, -1, -1
    dict_ = {}
    with open(filename, 'r') as csvfile:
        roster = csv.reader(csvfile, delimiter=',')
        for row in roster:
            if -1 in [name_idx, email_idx, uid_idx]:
                row_lowercase = [e.lower() for e in row]
                if name.lower() in row_lowercase:
                    name_idx = row_lowercase.index(name.lower())
                if email.lower() in row_lowercase:
                    email_idx = row_lowercase.index(email.lower())
                if uid.lower() in row_lowercase:
                    uid_idx = row_lowercase.index(uid.lower())
            elif len(row) > max(uid_idx,name_idx,email_idx):
                dict_[row[uid_idx].replace('-', '')] = [row[name_idx], row[email_idx].lower()]
    return dict_

def read2(filename,name,email, role):
    print "Reading roster " + filename
    name_idx, email_idx, role_idx = -1, -1, -1
    dict_ = {}
    with open(filename, 'r') as csvfile:
        roster = csv.reader(csvfile, delimiter=',')
        for row in roster:
            if -1 in [name_idx, email_idx, role_idx]:
                row_lowercase = [e.lower() for e in row]
                if name.lower() in row_lowercase:
                    name_idx = row_lowercase.index(name.lower())
                if email.lower() in row_lowercase:
                    email_idx = row_lowercase.index(email.lower())
                if role.lower() in row_lowercase:
                    role_idx = row_lowercase.index(role.lower())
            elif len(row) > max(name_idx, email_idx, role_idx) and row[role_idx] == 'Student':
                dict_[row[email_idx].lower()] = row[name_idx]
    return dict_

def main():
    args = parser.parse_args()
    myucladict = read1(args.myucla, 'Name', 'E-mail', 'UID')
    gradescopedict = read1(args.gradescope, 'Name', 'Email', 'SID')
    piazzadict = read2(args.piazza,'name', 'email','role')

    # enrolled but not in gradescope
    not_in_gradescope = set(myucladict.keys()) - set(gradescopedict.keys())
    # in gradescope but not enrolled
    in_gradescope_not_enrolled = set(gradescopedict.keys()) - set(myucladict.keys())

    # enrolled but not in piazza: either email or name matched will be labelled as "match"
    not_in_piazza = set()
    for uid in myucladict.keys():
        matched = False
        if myucladict[uid][1] in piazzadict.keys():
            matched = True
        else: 
            for name in piazzadict.values():
                if match_names(myucladict[uid][0], name):
                    matched = True
                    break
        if not matched:
            not_in_piazza.add(uid)

    # in piazza but not enrolled: either email or name matched will be labelled as "match"
    in_piazza_not_enrolled = set()
    for email_p in piazzadict.keys():
        matched = False
        for (name,email_m) in myucladict.values():
            if (email_p == email_m) or (match_names(piazzadict[email_p], name)):
                matched = True
                break
        if not matched:
            in_piazza_not_enrolled.add(email_p)

    # write result file
    # UID, name, email, enrolled, not in gradescope, not in piazza
    with open(args.save, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=args.separator)
        writer.writerow(['UID', 'Name', 'Email', 'Enrolled?', 'In gradescope?', 'In piazza?'])
        for key in not_in_gradescope:
            writer.writerow([key, myucladict[key][0].replace(',',''), myucladict[key][1],'yes', 'no', '-'])
        for key in not_in_piazza:
            writer.writerow([key, myucladict[key][0].replace(',',''), myucladict[key][1],'yes', '-', 'no'])

        for key in in_gradescope_not_enrolled:
            writer.writerow([key, gradescopedict[key][0], gradescopedict[key][1],'no', 'yes', '-'])
        for key in in_piazza_not_enrolled:
            writer.writerow(['-', piazzadict[key], key,'no', '-', 'yes'])
    print "Complete! Result file saved to "+ args.save
    print "Please open the result csv file using separator: " + args.separator

if __name__ == "__main__":
    main()