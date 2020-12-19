#Error messages
error_invalid_number = 'ERROR: negative or null prices are not allowed'
error_not_a_number = "ERROR: you must enter a numeric number"
menuError = "Please enter a valid option (1-5)"
lightError = "Types of light available: White, Blue and Yellow"
tag = 'Not available at this time, try again later.'
noProducts= "INFO: there are no products in the catalog"
#constants
vat_value = 0.21

#functions
#functions
def tryN(value):
    notaFloat = 0
    try:
        float(value)
    except:
        print(error_not_a_number)
        notaFloat = 1
    return(notaFloat)
def print_error(error_message):
    print(error_message)


def print_menu():
    print("************ MAIN MENU ************")
    print("\t1. Enter new product")
    print("\t2. Show catalog")
    print("\t3. Show most expensive product")
    print("\t4. Buy product")
    print("\t5. Exit")
    menuOption = input('\nSelect an option:')
    return(menuOption)


def check_error(menuOption):
    if tryN(menuOption)!= 1:
        menuOption = int(menuOption)
        if 0 < menuOption < 6 and type(menuOption) is int:
            return (False)
        else:
            print(menuError)
            return (True)


def is_positiveReal(num):
    if tryN(num)!= 1:
        num = float(num)
        if num > 0 :
            return (True)
        else:
            print(error_invalid_number)
            return (False)
            
    else:
            return (False)

def vat_calculation(num):
    sol = num + (num * vat_value)
    return (sol)


def light_type_validator(light):
    global lightTypeList
    lightTypeList = ['Yellow', 'White', 'Blue']
    if light in lightTypeList:
        return (True)
    else:
        print_error(lightError)
        return (False)


def fancy_print(objects):
    if len(products)== 0 :
        print(noProducts+ "\n")
    #Cada array tiene 8 valores
    else:
        for product in objects:
            print("Product #" + str(objects.index(product) + 1))
            print("\tName: " + str(product[0]))
            print("\tType of Product: " + str(product[1]))
            print("\tColor: " + str(product[2]))
            print("\tPower: " + str(product[3]))
            print("\tType of Light: " + str(product[4]))
            print("\tPrice without VAT: " + str(product[5]))
            print("\tPrice with VAT: " + str(product[6]))
            print("\tUnits: " + str(product[7]))
            print()

def addProduct():
    print('\nYou have selected ENTER NEW PRODUCT')
    # picks data of the product
    print('Enter he information for product #'+str(len(products) + 1)+"\n")
    newProduct = []
    name = input('Name of the product: ')
    newProduct.insert(0, name)
    typeProduct = input('Type of product: ')
    newProduct.insert(1, typeProduct)
    # loop for color validation
    colorValid = 0
    while colorValid == 0:
     
        print(
            'Colours available: White, Pearl white, Aluminium or Black'
        )
        colour = input('Colour of the product: ')
        if colour == "White" or colour == "Pearl white" or colour == "Aluminium" or colour == "Black":
            newProduct.insert(2, colour)
            break
        else:
            print('Error, colour not allowed')
    
    #loop for power validation
    powerValid = 0
    while powerValid == 0:
        power = input('Power (kW):')
        if tryN(power)!= 1:
            if is_positiveReal(power):
                power = float(power)
                newProduct.insert(3, power)
                powerValid = 1
    
    lightTypeValid = 0
    print(lightError)
    while lightTypeValid == 0:
          lightType = input('Type of light:')
          if light_type_validator(lightType):
              newProduct.insert(4, lightType)
              lightTypeValid = 1
    
    
    # loop for price validation
    priceValid = 0
    while priceValid == 0:
        price = input('Price without VAT:')
        if is_positiveReal(price) :
            price = int(price)
            if price < 50:
                print('Low price')
            elif price < 100:
                print('Medium price')
            else:
                print('High price')
            newProduct.insert(5, price)
            priceValid = 1
    
    # price vat calculation
    strpriceVAT = str(vat_calculation(price)) + ' €'
    newProduct.insert(6, strpriceVAT)
    
    # loop for number of units validation
    numberValid = 0
    while numberValid == 0:
        numberManufactured = input('Number of units manufactured:')
        if is_positiveReal(numberManufactured):
            newProduct.insert(7, numberManufactured)
            numberValid = 1
        
    
    
    
    strPower = str(power)
    strPrice = str(price) + ' €'
    # prints the result
    print('\n*** PRODUCT ***\nName: '+name+'\nType of product: '+typeProduct+'\nColour: '+colour+'\nPower: '+strPower+'\nType of light: '+lightType+
          '\nPrice without VAT: '+strPrice +' ; Price with VAT: ' +strpriceVAT+ '\nNumber of units: '+numberManufactured+"\n")
    return(newProduct)

def mosteExpensiveProduct():
    if len(products) == 0:
        print(noProducts+"\n")
    else:
        prices = []
        for product in products:
            prices.append(product[5])
        max_price = max(prices)
        pos = prices.index(max_price) + 1
    
        print("The most expensive product is #"+str(pos)+" with a value of " + str(max_price)+' €')


# menu loop
inputValid = 0
products = []
while inputValid == 0:
    x=0
    x=print_menu()
    if check_error(x) != True:
        
        
        if x == '1':
            products.append(addProduct())
        
        elif x == '2':
            print('\nYou have selected SHOW CATALOG')
            fancy_print(products)
            

        elif x == '3':
            print("\nYou have selected SHOW MOST EXPENSIVE PRODUCT")
            mosteExpensiveProduct()

                
                
                

        elif x == '4':
            print('\nYou have selected BUY PRODUCT')
            print(tag+"\n")
            

        elif x == '5':
            print('\nYou have selected EXIT')

            inputValid = 1

