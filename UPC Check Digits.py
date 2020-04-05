def checkUPC():
    UPC_start = input("\nWhat is the first 11 digits of the UPC? ")
    if len(UPC_start) == 11:
        UPC = [char for char in UPC_start]
        
        #DOESN'T ADD UP

        ODD_SUM = 0
        EVEN_SUM = 0

        count = 0
        for number in UPC:
            if count % 2 == 0:
                ODD_SUM += int(number)
            count += 1

        count = 1
        for number in UPC:
            if count % 2 == 1:
                EVEN_SUM += int(number)
            count += 1

        M = (ODD_SUM*3+EVEN_SUM) % 10
        if M == 0:
            return UPC_start+'0'
        else:
            return UPC_start+str(10-M)
        
    else:
        print("THE UPC is too short")

repeat = 0

print('Welcome To UPC Chceck\n')
while repeat != 'stop':
    print("The full UPC is:", checkUPC())
    repeat = input("\nRely 'stop' to stop: ")
    