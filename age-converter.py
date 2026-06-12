# Program to convert age in years to years, months, and days

age_years = int(input("Enter your age in years: "))

# 1 year = 12 months
age_months = age_years * 12

# 1 year = 365 days (approx)
age_days = age_years * 365

print("\nYour Age Breakdown:")
print("Years :", age_years)
print("Months:", age_months)
print("Days  :", age_days)

