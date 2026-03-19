input_usd = float(input("Enter the amount in USD: "))

usd_to_bdt = 120
usd_to_euro = .90
usd_to_gbp = .70

bdt = input_usd * usd_to_bdt
euro = input_usd * usd_to_euro
gbp = input_usd * usd_to_gbp

print(f"\n--- Converted Result for ${input_usd} USD ---")
print(f"BDT {bdt:.2f}")
print(f"EURO {euro:.2f}")
print(f"GBP {gbp:.2f}")