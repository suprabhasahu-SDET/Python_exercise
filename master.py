Total = 10000
Effort = 3

Days = Total // Effort
Rem_hrs = Total % Effort
Months = Days // 30
Days = Days % 30
Years = Months // 12
Months = Months % 12

print(Years, "yrs", Months, "mth", Days, "dys", Rem_hrs, "hrs")
