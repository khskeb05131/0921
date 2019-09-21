y = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
z = ['Annie','Betty','Claire','Daphne','Ellie',\
     'Franchesca','Greta','Holly','Isabel','Jenny']
another_dict = {'x':'printer','y':5,'z':['star','circle',9]}

for month in y:
    print("{!s}".format(month))

for i in range(len(z)):
    print("{0}: {1}".format(i, z[i]))

for j in range(len(y)):
    if y[j].startswith('J'):
        print("{}".format(y[j]))

for key, value in another_dict.items():
    print("{},{}".format(key,value))
