# Function with if condition to check if there's an overtime to calculate or not, and calculate it based on the hours
def computepay(Hours, Rate):
    if Hours > 40:
        OverTimeHours = Hours - 40
        Hours = 40
        BasicPay = Hours * Rate
        OverTimePay = OverTimeHours * OverTimeRate
        TotalPay = BasicPay + OverTimePay
    else:
        TotalPay = Hours * Rate
    return TotalPay


# Inputs for hours and rate with float
Hours = float(input('Enter The Hours'))
Rate = float(input('Enter The Hourly Rate'))
OverTimeRate = Rate*1.5

# printing the output with calling the computepay function
print('Pay', computepay(Hours, Rate))
