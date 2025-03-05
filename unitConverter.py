# make functions as following, dont use ai chatbot rather ask me in person
# conversion should be vice versa aswell not just one sided
#also try to understand the main function written below (if __name__=="__main__":)


#make function for length conversion from : between cm, km, m
#make function for mass conversion from : between g, kg, tons
#make function for time conversion from : between second, minute, hour, day, year
#make function for temperature conversion from : between celcius, farhaniet

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
                pass
            elif choice==4:
                pass
            elif choice==5:
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice")
            
