# make functions as following, dont use ai chatbot rather ask me in person
# conversion should be vice versa aswell not just one sided
# also try to understand the main function written below (if __name__=="__main__":)
# make function for length conversion from : between cm, km, m
# make function for mass conversion from : between g, kg, tons
def mass_conversion():
    from_unit = input("Enter 'from' unit (milligram, gram, kilogram, tons) : ")
    to_unit = input("Enter 'to' unit (milligram, gram, kilogram, tons) : ")
    value = int(input("Enter the value : "))
    if from_unit=="kilogram":
        value *=1000
    elif from_unit=="milligram":
        value /=1000
    elif from_unit=="tons":
        value *=1000000
    elif from_unit=="gram":
        pass
    else:
        print("Invalid 'from' unit")

    #now the value is in grams
    if (to_unit.strip()).lower()=="kilogram":
        value/=1000
    elif (to_unit.strip()).lower()=="milligram":
        value*=1000
    elif (to_unit.strip()).lower()=="tons":
        value/=1000000
    elif (to_unit.strip()).lower()=="gram":
        pass
    else:
        print("Invalid 'to' unit")
    print(f"value is {value} {to_unit}\n")
# make function for time conversion from : between second, minute, hour, day, year
# make function for temperature conversion from : between celcius, farhaniet
if __name__=="__main__":
    while True:
        try:
            print("Piba's Unit Converter!!")
            choice = int(input("1. Length\n2. Temperature\n3. Mass\n4. Time\n5. Exit Program\nEnter your Choice number:"))
            if choice == 1:
                pass
            elif choice==2:
                pass
            elif choice==3:
                mass_conversion()
            elif choice==4:
                pass
            elif choice==5:
                print("program exited successfully")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice")