#Best case scenario
weekends = 52 / 2 #  Days
close_bdays = 5 + 3 + 2
family_functions = 5 + 2
holiday = 5
total_hours_min = 2 *(weekends + close_bdays + family_functions) # 2 Hours per gathering
total_hours_max = 5 *(weekends + close_bdays + family_functions) # 5 Hours per gathering

#Realistic
realistic_weekends = 12 # 12 Days
realistic_close_bdays = 5 + 2
realistic_family_functions = 3
realistic_holiday = 2
realistic_total_hours_min = 2 *(realistic_weekends + realistic_close_bdays + realistic_family_functions) # Hours per gathering
realistic_total_hours_max = 5 *(realistic_weekends + realistic_close_bdays + realistic_family_functions) # Hours per gathering

#Future: Holiday in ZA w/Euro 
future_holiday = 30
future_total_hours_min = 5 *(future_holiday) #  Hours per gathering
future_total_hours_max = 12 *(future_holiday) #  Hours per gathering

#Future: Family in EU
eu_future_holiday = 20
eu_future_total_hours_min = 5 *(eu_future_holiday) #  Hours per gathering
eu_future_total_hours_max = 12 *(eu_future_holiday) #  Hours per gathering

#Future: Potential Time With Family Throughout 1 Year
future_total_days_year = (future_holiday + eu_future_holiday)
future_total_min_hours_year = (future_total_hours_min + eu_future_total_hours_min)
future_total_max_hours_year = (future_total_hours_max + eu_future_total_hours_max)

#BestCase

print("\nBest Scenario: Living in same country\n")

print(f"Total days with family: {weekends + close_bdays + family_functions + holiday:.2f} Days\n")

print(f"Total Min Hours Spent together (2 Hour Avg Per Gathering): {total_hours_min:.2f} | {total_hours_min / 24:.2f} Days\n")

print(f"Total Max Hours Spent together (5 Hour Avg Per Gathering): {total_hours_max:.2f} | {total_hours_max / 24:.2f} Days\n")

#Worstcase

print("\nRealistic Scenario: Living in same country\n")

print(f"Total days with family: {realistic_weekends + realistic_close_bdays + realistic_family_functions + realistic_holiday:.2f} Days\n")

print(f"Total Min Hours Spent together (2 Hour Avg Per Gathering): {realistic_total_hours_min} Hours | {realistic_total_hours_min / 24:.2f} Days\n")

print(f"Total Max Hours Spent together (5 Hour Avg Per Gathering): {realistic_total_hours_max} Hours | {realistic_total_hours_max / 24:.2f} Days\n")


#Future w/Euro in ZA

print("\nFuture: Holiday in ZA with EU\n")

print(f"Total days with family: {future_holiday:.2f} Days\n")

print(f"Total Min Hours Spent together (5 Hour Avg Per Gathering): {future_total_hours_min} Hours | {future_total_hours_min / 24:.2f} Days\n")

print(f"Total Max Hours Spent together (12 Hour Avg Per Gathering): {future_total_hours_max} Hours | {future_total_hours_max / 24:.2f} Days\n")

#Future: Family Visit in EU

print("\nFuture: Family Holiday in EU\n")

print(f"Total days with family: {eu_future_holiday:.2f} Days\n")

print(f"Total Min Hours Spent together (5 Hour Avg Per Gathering): {eu_future_total_hours_min} Hours | {eu_future_total_hours_min / 24:.2f} Days\n")

print(f"Total Max Hours Spent together (12 Hour Avg Per Gathering): {eu_future_total_hours_max} Hours | {eu_future_total_hours_max / 24:.2f} Days\n")

#Future: Total per yar

print("\nFuture: Potential Time With Family Throughout 1 Year\n")

print(f"Total days with family in 1 year {eu_future_holiday + future_holiday:.2f} Days\n")

print(f"Total Min Hours Spent together (5 Hour Avg Per Gathering): {future_total_min_hours_year} Hours\n")

print(f"Total Max Hours Spent together (12 Hour Avg Per Gathering): {future_total_max_hours_year} Hours\n")