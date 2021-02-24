def swap():
    f1 = input('Enter file 1 name:- ')
    f2 = input('Enter file 2 name:- ')
    with open(f1,'r') as a:
        da = a.read()
    with open(f2,'r') as b:
        db = b.read()
    with open(f1,'w') as a:
        a.write(db)
    with open(f2,'w') as b:
        b.write(da)
    print('The data of the two file is ')
swap()