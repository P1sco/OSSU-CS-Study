Hours = float(input("Enter Hours:"))
Rate = float(input("Enter Hourly Rate:"))
OverTimeRate = Rate*1.5
if Hours > 40:
    OverTime = Hours - 40
    Hours = 40
BasicPay = Hours * Rate
OverTimePay = OverTime * OverTimeRate
TotalPay = OverTimePay + BasicPay
print(TotalPay)
