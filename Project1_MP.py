# -----------------------------------------------------------------
# Assignment Name: Project1_MP 
# Name: Mitch Puma
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# Function Name:        Validate String Input
# Function Purpose:     Validate any String data
# -----------------------------------------------------------------
def Validate_String_Input( str_Input ):
    
   if(str_Input == 'M') or (str_Input == 'E'):
      global strValidated
      strValidated = True
   else:
      print("Employee must be 'M' or 'E'")
   
   return str_Input



# -----------------------------------------------------------------
# Function Name:        Validate Integer Input
# Function Purpose:     Validate any integer data
# -----------------------------------------------------------------
def Validate_Integer_Input( int_Input ):
   try:
        int_Input = int(int_Input)
        if(int_Input >= 0):
            global strValidated
            strValidated = True
        else:
            print("Input Must Be 0 or More")
   except ValueError:
        int_Input = int(0)
        print("Input Must be Numeric")
   return int_Input



# -----------------------------------------------------------------
# Function Name:        Validate Float Input
# Function Purpose:     Validate any Float data
# -----------------------------------------------------------------
def Validate_Float_Input( flt_Input ):
   try:
        flt_Input = float(flt_Input)
        if(flt_Input >= 0):
            global strValidated
            strValidated = True
        else:
            print("Input Must Be 0 or More")
   except ValueError:
        flt_Input = int(0)
        print("Input Must be Numeric")
   return flt_Input



# -----------------------------------------------------------------
# Function Name: Calculate_Employee_Discount()
# Function Purpose: Calculate the employee's discount.
# -----------------------------------------------------------------
def Calculate_Employee_Discount(intYears, strEmployment):
    dblDiscount = float(0)
    if(strEmployee == 'M'):
        dblDiscount += 0.1
    if(intYears >= 16):
        dblDiscount += 0.3
    else:
        if(intYears >= 11):
            dblDiscount += 0.25
        else:
            if(intYears >= 7):
                dblDiscount += 0.2
            else:
                if(intYears >= 4):
                    dblDiscount += 0.14
                else:
                    dblDiscount += 0.1
    return dblDiscount



# -----------------------------------------------------------------
# Function Name: Calculate_DiscountYTD
# Function Purpose: Calculate product of amount of money (YTD) employee has spent & discount.
# -----------------------------------------------------------------
def Calculate_DiscountYTD(dblYearsToDollar, dblDiscount):
    dblDiscountYTD = float(0)
    dblDiscountYTD = dblYearsToDollar * dblDiscount
    return dblDiscountYTD



# -----------------------------------------------------------------
# Function Name: Calculate_Discount_Total
# Function Purpose: Calculate the amount of money the employee is able to use from discount on final purchase.
# -----------------------------------------------------------------
def Calculate_Discount_Total(intYTDMax, dblDiscountYTD, dblSubtotal, dblTodaysPurchaseTotal):
    dblDiscountTotal = float(0)
    if(dblDiscountYTD >= intYTDMax):
        dblDiscountTotal = 0
    else:
        if((dblDiscountYTD + dblTodaysPurchaseTotal) < intYTDMax):
            dblDiscountTotal = dblSubtotal
        if((dblDiscountYTD + dblTodaysPurchaseTotal) >= intYTDMax):
            dblDiscountTotal = (intYTDMax - dblDiscountYTD)
    return dblDiscountTotal



# -----------------------------------------------------------------
# Function Name: Calculate_Subtotal
# Function Purpose: Calculate the subtotal that will be used to if the entire discount is able to be used on purchase.
# -----------------------------------------------------------------
def Calculate_Subtotal(dblPurchase, dblDiscount):
    dblSubtotal = float(0)
    dblSubtotal = dblPurchase * dblDiscount
    return dblSubtotal



# -----------------------------------------------------------------
# Function Name: Calculate_Todays_Total_Purchase
# Function Purpose: Calculate how much was spent today with the purchase amount and discount percentage.
# -----------------------------------------------------------------
def Calculate_Todays_Total_Purchase(dblPurchase, dblSubtotal):
    dblTodaysPurchaseTotal = float(0)
    dblTodaysPurchaseTotal = (dblPurchase - dblSubtotal)
    return dblTodaysPurchaseTotal



# -----------------------------------------------------------------
# Function Name: Calculate_Total_With_Discount 
# Function Purpose: Calculate the final total with discount allowed subtracted from purchase.
# -----------------------------------------------------------------
def Calculate_Total_With_Discount(dblPurchase, dblDiscountTotal):
    dblTotalWithDiscount = float(0)
    dblTotalWithDiscount = dblPurchase - dblDiscountTotal
    return dblTotalWithDiscount



# -----------------------------------------------------------------
# Function Name: Employee_Summary
# Function Purpose: Ask the user if they want to end the program and display all employee summary.
# -----------------------------------------------------------------
def Employee_Summary(dblEmpSumPurchase, dblEmpSumTotalWithDiscount, strAnotherEmployee):
    strEmpSumPurchase = "${:,.2f}".format(dblEmpSumPurchase)
    strEmpSumTotalWithDiscount = "${:,.2f}".format(dblEmpSumTotalWithDiscount)
    strAnotherEmployee = bool(True)
    strValidated = bool(False)
    strEmployee = str("")

    while strValidated is False:
        strEmployee = input("Another Employee 'YES' or 'NO' ")
        strValidated = Validate_String_Input_Exit (strEmployee)
    if(strEmployee == 'NO'):
        print("a. Total before discount for the day", strEmpSumPurchase)
        print("b. Total after discounts applied ", strEmpSumTotalWithDiscount)
        strAnotherEmployee = False
    return strAnotherEmployee




# -----------------------------------------------------------------
# Function Name: Validate String Input Exit
# Function Purpose: Validate any String data to exit the program.
# -----------------------------------------------------------------
def Validate_String_Input_Exit( strEmployment ):
   
   strValidated = bool(False)
   if(strEmployment == 'YES') or (strEmployment == 'NO'):
      strValidated = True
   else:
      print("Employee must be 'YES' or 'NO'")
   
   return strValidated



# -----------------------------------------------------------------
# Function Name: Display_Totals
# Function Purpose: Display Totals
# -----------------------------------------------------------------
def Display_Totals(dblDiscount, dblDiscountYTD, dblTodaysPurchaseTotal, dblDiscountTotal, dblTotalWithDiscount):
    strDiscount =  "%{:,.2f}".format(dblDiscount * 100)
    strDiscountYTD = "${:,.2f}".format(dblDiscountYTD)
    strTodaysPurchaseTotal = "${:,.2f}".format(dblTodaysPurchaseTotal)
    strDiscountTotal = "${:,.2f}".format(dblDiscountTotal)
    strTotalWithDiscount = "${:,.2f}".format(dblTotalWithDiscount)
    print("a.Employee discount percentage ", strDiscount)
    print("b.YTD Amount of discount in dollars ", strDiscountYTD)
    print("c.Total purchase today before discount", strTodaysPurchaseTotal)
    print("d.Employee discount this purchase ", strDiscountTotal)
    print("e.Total with discount ", dblTotalWithDiscount)



# -----------------------------------------------------------------
# Name:                 Controlling Main Code for Applications
# Purpose:              Controls the flow for Discount Program Application
# -----------------------------------------------------------------

# declare all input, output, and other needed variables
dblEmpSumPurchase = float(0)
dblEmpSumTotalWithDiscount = float(0)
strAnotherEmployee = bool(True)
while strAnotherEmployee is True:
    intYTDMax = int(200)
    intYears = int(0)
    dblYearsToDollar = float(0)
    strEmployment = str("")
    dblPurchase = float(0)

    dblDiscount = float(0)
    dblDiscountYTD = float(0)
    dblSubtotal = float(0)
    dblTodaysPurchaseTotal = float(0)
    dblDiscountTotal = float(0)
    dblTotalWithDiscount = float(0)

    strValidated = bool(False)

    # loop until input is valid
    while strValidated is False:
        strEmployee = input("Type of Employee 'M' or 'E' ")
        strEmployee = Validate_String_Input (strEmployee) 

    strValidated = bool(False)
    while strValidated is False:
        intYears = input("Enter the number of years as an integer. ")
        intYears = Validate_Integer_Input (intYears) 

    strValidated = bool(False)
    while strValidated is False:
        dblYearsToDollar = input("Enter the total amount of money spent this year. ")
        dblYearsToDollar = Validate_Float_Input (dblYearsToDollar) 

    strValidated = bool(False)
    while strValidated is False:
        dblPurchase = input("Enter today's purchase total. ")
        dblPurchase = Validate_Float_Input (dblPurchase) 

    # call functions to calculate
    dblDiscount = Calculate_Employee_Discount(intYears, strEmployment)
    dblDiscountYTD = Calculate_DiscountYTD(dblYearsToDollar, dblDiscount)
    dblSubtotal = Calculate_Subtotal(dblPurchase, dblDiscount)
    dblTodaysPurchaseTotal = Calculate_Todays_Total_Purchase(dblPurchase, dblSubtotal)
    dblDiscountTotal = Calculate_Discount_Total(intYTDMax, dblDiscountYTD, dblSubtotal, dblTodaysPurchaseTotal)
    dblTotalWithDiscount = Calculate_Total_With_Discount(dblPurchase, dblDiscountTotal)
    dblEmpSumPurchase += dblPurchase
    dblEmpSumTotalWithDiscount += dblTotalWithDiscount
    # call function to format and display
    Display_Totals(dblDiscount, dblDiscountYTD, dblTodaysPurchaseTotal, dblDiscountTotal, dblTotalWithDiscount)
    strAnotherEmployee = Employee_Summary(dblEmpSumPurchase, dblEmpSumTotalWithDiscount, strAnotherEmployee)
