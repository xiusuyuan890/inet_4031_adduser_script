#!/usr/bin/python3
#John Xiu
#Automating User Management
#November 5, 2024
#November 6, 2024


#"import OS" allows the python script to interact with the operating system.
import os
import re
import sys

def main():
    for line in sys.stdin:

        #this "regular expression" is searching for any line that starts with the "#"
        match = re.match("^#",line)

        #The "line.strip" removes the leading and trailing whitespace from the line, and "split" splits the stripped line into a list of substrings using ":" as the delimiter
        fields = line.strip().split(':')

        #This IF statement is checking  if the line it's reading is a comment, and if it does not contain exactly 5 fields.
        #If the IF statement evaluates to be true, then the "continue" statement is executed, which means it will skip that line
        #The "match" is set to check if the line starts with "#", and "fields" is created by splitting the line on ":". So the IF statement uses match to skip lines that are comment, and fields to skip lines that don't have exactly 5 fields
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)

        for group in groups:
            #This IF statement is checking if the group  is not equal to "-". "-" might indicate that there is a placeholder or an empty group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
