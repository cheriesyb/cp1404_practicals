
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill estimator 2.0")

tariff_choice = input("Which tariff? 11 or 31: ")


daily_use_in_KWh = float(input("Enter daily use in KWh: "))
number_of_billing_days = int(input("Enter the number of billing days: "))
estimate_bill = tariff_choice * daily_use_in_KWh * number_of_billing_days
print("Estimated bill: ", estimate_bill)