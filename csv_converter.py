import sys
import os

def read(filename):
    with open(filename, 'r') as f:
        l = f.readlines()
        f.close
        return l
      

def convert(filename,x):
    with open(filename, 'w') as e:
         e.writelines(x)
         e.close
    newfile, ext = os.path.splitext(filename)
    os.rename(filename, newfile + ".xml")
    m = (newfile)
    return m




def output(z):
    print 'This is the new filename: %s ' % (z)
    


def main():
    y = ("""<Department>
<Record>
<StudentID>970100</StudentID>
<FirstName>Tom</FirstName>
<LastName>Smith</LastName>
</Record>
<Record>
<StudentID>970101</StudentID>
<FirstName>David</FirstName>
<LastName>Washington</LastName>
</Record>
</Department>""")
    filename = (sys.argv[1])
    x = read(filename)
    x = y
    z = convert(filename,x)
    output(z)



if __name__ == "__main__":
    main()





