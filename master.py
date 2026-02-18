Total = 10000
#Effort = 4
Effort = int(input("what is your daily effort? "))

Days = Total // Effort
Rem_hrs = Total % Effort
Months = Days // 30
Rem_days = Days % 30
Years = Months // 12
Rem_months = Months % 12

print(Years, "yrs", Rem_months, "mth", Rem_days, "dys", Rem_hrs, "hrs")
