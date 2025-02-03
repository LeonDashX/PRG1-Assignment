#Joshua Leong Shao En (S10258327)


#directory
path = 'C:\\Users\joshu\OneDrive\Desktop\Poly stuff lol\y1s1\PRG\Assignment\\'

#global variables for dictionaries in list
dict_info = []
dict_v = []
global_name = ''
#global variable to check if option 3 has been done before or not
check = 0

#adding list of values into the lines list
with open(path + 'carpark-information.csv','r') as info:
    a = info.readlines()
    title = a[0].strip('\n').split(',')
    a.remove(a[0])
    for i in a:
        b = {}
        i = i.strip('\n')
        i = i.split(',',3)
        if '"' in i[-1]:
            i[-1] = i[-1].strip('"')
        for j in range(4):
            b[title[j]] = i[j]
        dict_info.append(b)



#defines function for the menu
def menu():
    opt = input(("\nMENU\n\
====\n\
[1] Display Total Number of Carparks in 'carpark-information.csv'\n\
[2] Display All Basement Carparks in 'carpark-information.csv'\n\
[3] Read Carpark Availability Data File\n\
[4] Print Total Number of Carparks in the File Read in [3]\n\
[5] Display Carparks Without Available Lots\n\
[6] Display Carparks With At Least x% Available Lots\n\
[7] Display Addresses of Carparks With At Least x% Available Lots\n\
[8] Display Carpark Information at Specific Location\n\
[9] Display Information on the Carpark with Most Lots\n\
[10] Create a file containing Carpark Number, Total Lots, Lots Available, and Address\n\
[0] Exit\n\
Enter your option: "))
    return opt

#defines function for option 1
def opt1():
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
    print("Total Number of carparks in 'carpark-information.csv': {}.".format(len(dict_info))) #calculates number of carparks
    
#defines function for option 2
def opt2():
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    bm = 0 #bm represents the number of basement carparks
    bm_lis = [] #list to contain list of basement carparks 
    #goes through all lists in the dict_info to find basement carparks
    for i in dict_info:
        if 'basement' in i['Carpark Type'].lower(): #checks if carpark is basement 
            bm += 1
            bm_lis.append(i)
    print("{} {:<18} {}".format('Carpark No','Carpark Type','Address'))
    for i in range(bm):
        print("{:<10} {:<18} {}".format(bm_lis[i]['Carpark Number'],bm_lis[i]['Carpark Type'],bm_lis[i]['Address']))
    print("Total number: {}".format(bm))

#defines function for option 3
def opt3():
    print("Option 3: Read Carpark Availability Data File")
    path = 'C:\\Users\joshu\OneDrive\Desktop\Poly stuff lol\y1s1\PRG\Assignment\\' #directory
    #input validation
    while True:
        name = input("Enter the file name: ")
        try:
            file = open(path + name,"r")
            break
        except:
            print("File not found!")
    file = open(path + name,"r") #opens file entered by user
    data = file.readlines()
    #creates list of dictionaries
    if global_name != name or global_name != '':
        dict_v.clear()
    with open(path + name,'r') as info:
        a = info.readlines()
        a.remove(a[0])
        title = a[0].strip('\n').split(',')
        a.remove(a[0])
        for i in a:
            b = {}
            i = i.strip('\n')
            i = i.split(',')
            for j in range(3):
                b[title[j]] = i[j]
            dict_v.append(b)
    print("Timestamp: {}".format(data[0])) #prints first row of the spreadsheet containing the timestamp
    return name

#defines function for option 4
def opt4():
    if check: #checks if option 3 has been done before
        print("Option 4: Print Total Number of Carparks in the File Read in [3]")
        print('Total Number of Carparks in the File: {}'.format(len(dict_v))) #calculates number of carparks (number of rows)
    else:
        print("Must you option 3 first!") #tells user to do option 3 first

#defines function for option 5
def opt5():
    count = 0 #variable for the number of carparks without available lots
    if check: #checks if option 3 has been done before
        print("Option 5: Display Carparks Without Available Lots")
        for i in dict_v:
            if i['Lots Available'] == '0':
                print("Carpark Number: {}".format(i['Carpark Number']))
                count += 1
        print("Total number: {}".format(count))
    else:
        print("Must you option 3 first!") #tells user to do option 3 first

#defines function for option 6
def opt6():
    count = 0 #variable for the number of carparks that meet the minimum percentage for available lots
    if check: #checks if option 3 has been done before
        print("Option 6: Display Carparks With At Least x% Available Lots")
        #input validation
        while True:
            minimum = input("Enter the percentage required: ")
            try:
                float(minimum)
                if 0<=float(minimum)<=100:
                    break
                else:
                    print("Number must be between 0 and 100!")
            except:
                print("Enter a number!")
        minimum = float(minimum)
        print("{:<11} {:<11} {:<15} {}".format('Carpark No','Total Lots','Lots Available','Percentage'))
        for i in dict_v:
            if int(i['Total Lots']) != 0:
                if (int(i['Lots Available'])/int(i['Total Lots']))*100 >= minimum: #checks if percentage meets minimum entered
                    print("{:<5} {:>16} {:>15} {:>11.1f}".format(i['Carpark Number'],i['Total Lots'],i['Lots Available'],(int(i['Lots Available'])/int(i['Total Lots']))*100))
                    count += 1
        print("Total number: {}".format(count))
    else:
        print("Must you option 3 first!") #tells user to do option 3 first

#defines function for option 7
def opt7():  
    count = 0 #checks if option 3 has been done before
    if check:
        print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")  
        #input validation
        while True:
            minimum = input("Enter the percentage required: ")
            try:
                float(minimum)
                if 0<=float(minimum)<=100:
                    break
                else:
                    print("Number must be between 0 and 100!")
            except:
                print("Enter a number!")
        minimum = float(minimum)
        
        print("{:<11} {:<11} {:<15} {:<11} {}".format('Carpark No','Total Lots','Lots Available','Percentage','Address'))
        for i in dict_v:
            if int(i['Total Lots']) != 0: #prevents division by zero error
                if (int(i['Lots Available'])/int(i['Total Lots']))*100 >= minimum: #checks if percentage meets minimum entered
                    for j in dict_info:
                        if i['Carpark Number'] == j['Carpark Number']:
                            address = j['Address']
                            break
                    print("{:<5} {:>16} {:>15} {:>11.1f}  {}".format(i['Carpark Number'],i['Total Lots'],i['Lots Available'],(int(i['Lots Available'])/int(i['Total Lots']))*100,address))
                    count += 1
        print("Total number: {}".format(count))
    else:
        print("Must you option 3 first!")

#defines function for option 8
def opt8():
    if check: #checks if option 3 was done before
        count = 0 #count variable counts total number of carparks at specified location
        print("Option 8: Display Carpark Information at Specific Location")
        #input validation
        while True:
            location = input("Enter desired location: ")
            if ' ' in location:
                if location.replace(' ','').isalpha():
                    break
                else:
                    print("Enter a word!")
            elif location.isalpha():
                break
            else:
                print("Enter a word!")
        print("{:<11} {:<11} {:<15} {:<11} {}".format('Carpark No','Total Lots','Lots Available','Percentage','Address'))
        for i in dict_info:
            #checks if location entered is in the address
            if location.upper() in i['Address']:
                address = i['Address'] #saves location in address variable
                for j in dict_v:
                    if j['Carpark Number'] == i['Carpark Number']:
                        if int(j['Total Lots']) != 0:
                            percentage = (int(j['Lots Available'])/int(j['Total Lots']))*100
                            print("{:<5} {:>16} {:>15} {:>11.1f}  {}".format(j['Carpark Number'],j['Total Lots'],j['Lots Available'],percentage,address))
                            count += 1
                            break
        if count > 0:
            print("Total number: {}".format(count))
        else:
            print("No carparks found.")
    else:
        print("Must you option 3 first!") #tells user to do option 3 first

#defines function for option 9
def opt9():
    print("Option 9: Display Information on the Carpark with Most Lots")
    most = 0 #variable to find the highest total lots
    car_num = 0
    total = 0
    available = 0
    path = 'C:\\Users\joshu\OneDrive\Desktop\Poly stuff lol\y1s1\PRG\Assignment\\' #directory
    with open(path + 'carpark-availability-v1.csv','r') as info:
        #creates list of dictionaries
        a = info.readlines()
        a.remove(a[0])
        title = a[0].strip('\n').split(',')
        a.remove(a[0])
        for i in a:
            b = {}
            i = i.strip('\n')
            i = i.split(',')
            for j in range(3):
                b[title[j]] = i[j]
            dict_v.append(b)
        for i in dict_v:
            if int(i['Total Lots']) > most:
                most = int(i['Total Lots']) #replaces value inside if int(i['Total Lots']) is bigger than the current value
                car_num = i['Carpark Number']
                total = int(i['Total Lots'])
                available = int(i['Lots Available'])
        print("{:<12} {:<23} {:<20} {:<11} {:<16} {:<12} {}".format('Carpark No','Carpark Type','Parking System','Total Lots','Lots Available','Percentage','Address'))
        for j in dict_info:
            if j['Carpark Number'] == car_num:
                Type = j['Carpark Type']
                System = j['Type of Parking System']
                Address = j['Address']
        print("{:<12} {:<23} {:<20} {:<11} {:<16} {:<12.1f} {}".format(car_num,Type,System,total,available,(available/total)*100,Address))

#defines function for option 10
def opt10():
    if check: #checks if option 3 has been done before
        file = open(path + "carpark-availability-with-addresses.csv",'x') #creates file
        print("Option 10: Create a file containing Carpark Number, Total Lots, Lots Available, and Address")
        file.write('Carpark Number,Total Lots,Lots Available,Address')
        for i in dict_v:
            address = ''
            for j in dict_info:
                if j['Carpark Number'] == i['Carpark Number']:
                    address = j['Address']
                    break
                if address == '': #prints out '-' if there is no address to the carpark number
                    address = '-'
            file.write('\n{},{},{},{}'.format(i['Carpark Number'],i['Total Lots'],i['Lots Available'],address))
        file = open(path + "carpark-availability-with-addresses.csv",'r')
        print("Filename: {}\nNumber of lines: {}".format("carpark-availability-with-addresses.csv",len(file.readlines())))
    else:
        print("Do option 3 first!") #tells user to do option 3 first

while True: #loops the menu
    opt = menu()
    if opt == '1':
        opt1()
    elif opt == '2':
        opt2()
    elif opt == '3':
        global_name = opt3()
        check += 1
    elif opt == '4':
        opt4()
    elif opt == '5':
        opt5()
    elif opt == '6':
        opt6()
    elif opt == '7':
        opt7()
    elif opt == '8':
        opt8()
    elif opt == '9':
        opt9()
    elif opt == '10':
        opt10()
    elif opt == '0':
        break
    elif not opt.isdigit(): #checks if input is not a number
        print("\nPlease enter a number.")
    elif not 0<int(opt)<10: #checks if input is not in range of the options
        print("\nPlease enter a number from one of the options.")

