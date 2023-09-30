def reader(filename):
        total=0
        f = open(filename, "r")
        for line in f:
            tokens=line.strip().split()
            length=len(tokens)
            if length!=5:
                return False
            try:
                int(tokens[0])
                int(tokens[2])
                int(tokens[3])
                float(tokens[4])
            except:
                return False
            total+=float(tokens[-1])
        f.close()
        return (int(tokens[0]), tokens[1], int(tokens[2]), int(tokens[3]), int(tokens[4]))



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))