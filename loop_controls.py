numbers = [56, 45, 77, 109, 98]
for number in numbers:
    if number == 77:
        break
    print(number)

numbers = [56, 45, 77, 109, 98]
for number in numbers:
    if number == 77:
        continue
    print(number)

log_file = [
    "INFO: Operation successful",
    "ERROR: File not found",
    "DEBUG: Connection established",
    "ERROR: Database connection failed",
]

for line in log_file:
    if "ERROR" in line:
        print(line)
