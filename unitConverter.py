# make functions as following, dont use ai chatbot rather ask me in person
# conversion should be vice versa aswell not just one sided
#also try to understand the main function written below (if __name__=="__main__":)


#make function for length conversion from : between cm, km, m
#make function for mass conversion from : between g, kg, tons
#make function for time conversion from : between second, minute, hour, day, year
#make function for temperature conversion from : between celcius, farhaniet
if __name__=="__main__":
    sec=1
    min1=60
    hour=3600
    day=86400
    year=31536000
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
                try:
                    print("Time conversion")
                    print("option 1: Second\noption 2: Minute\noption 3: Hour\noption 4: Day\noption 5: Year")
                    print("Enter the value you want to convert")
                    Value1 = int(input("Enter the value:"))
                    print("Select the unit you want to convert from")
                    input1 = int(input("Enter your choice:")) 
                    print("select the unit you want to convert to")
                    input2 = int(input("Enter your choice:"))
                    if input1 == 1:
                        if input2 == 2:
                            print(f"Conversion from Second to Minute is {sec*Value1/min1}")
                        elif input2 == 3:
                            print(f"Conversion from Second to Hour is {sec*Value1/hour}")
                        elif input2 == 4:
                            print(f"Conversion from Second to Day is {sec*Value1/day}")
                        elif input2 == 5:
                            print(f"Conversion from Second to Year is {sec*Value1/year}")
                        else:
                            print("Invalid Choice")
                    elif input1 == 2:
                        if input2 == 1:
                            print(f"Conversion from Minute to Second is {min1*Value1/sec}")
                        elif input2 == 3:
                            print(f"Conversion from Minute to Hour is {min1*Value1/hour}")
                        elif input2 == 4:
                            print(f"Conversion from Minute to Day is {min1*Value1/day}")
                        elif input2 == 5:
                            print(f"Conversion from Minute to Year is {min1*Value1/year}")   
                        else:
                            print("Invalid Choice")
                    elif input1 == 3:
                        if input2 == 1:
                            print(f"Conversion from Hour to Second is {hour*Value1/sec}")
                        elif input2 == 2:
                            print(f"Conversion from Hour to Minute is {hour*Value1/min1}")
                        elif input2 == 4:
                            print(f"Conversion from Hour to Day is {hour*Value1/day}")
                        elif input2 == 5:
                            print(f"Conversion from Hour to Year is {hour*Value1/year}")
                        else:
                            print("Invalid Choice")
                    elif input1 == 4:
                        if input2 == 1:
                            print(f"Conversion from Day to Second is {day*Value1/sec}")
                        elif input2 == 2:
                            print(f"Conversion from Day to Minute is {day*Value1/min1}")
                        elif input2 == 3:
                            print(f"Conversion from Day to Hour is {day*Value1/hour}")
                        elif input2 == 5:
                            print(f"Conversion from Day to Year is {day*Value1/year}")
                        else:
                            print("Invalid Choice")
                    elif input1 == 5:
                        if input2 == 1:
                            print(f"Conversion from Year to Second is {year*Value1/sec}")
                        elif input2 == 2:
                            print(f"Conversion from Year to Minute is {year*Value1/min1}")
                        elif input2 == 3:
                            print(f"Conversion from Year to Hour is {year*Value1/hour}")
                        else:
                            print("Invalid Choice")
                except ValueError:
                    print("Invalid Choice")
            elif choice==5:
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice")
            
