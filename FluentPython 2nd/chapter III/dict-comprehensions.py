
dial_codes = [(55, 'Brazil'),(86,'China'), (81,'Japan'),]
print(dial_codes[1])

country_codes = {country: code for code, country in dial_codes}

swaped_codes = {code: country.upper() for country, code in sorted(country_codes.items()) if code < 85}
print(country_codes.items())
print(swaped_codes)