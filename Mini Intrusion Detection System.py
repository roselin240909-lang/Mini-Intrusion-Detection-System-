import os

print("====================================")
print("       MINI INTRUSION DETECTION")
print("====================================")

if not os.path.exists("security_log.txt"):

    print("Security log file not found.")
    print("Please make sure security_log.txt is in the same folder.")

else:

    failed_attempts = {}

    file = open("security_log.txt", "r")

    for line in file:

        if "Login failed" in line:

            ip = line.split("IP: ")[1].strip()

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

    file.close()

    # Total failed attempts
    total_failed = 0

    for ip in failed_attempts:
        total_failed += failed_attempts[ip]

    print("Total Failed Login Attempts:", total_failed)

    # Failed login attempts by IP
    print("----------------------")
    print("Failed Login Attempts")

    for ip in failed_attempts:
        print(ip, ":", failed_attempts[ip])

    # Suspicious IP addresses
    print("----------------------")
    print("Suspicious IP Addresses")

    suspicious_found = False

    for ip in failed_attempts:

        if failed_attempts[ip] >= 3:
            print("⚠", ip, "is suspicious.")
            suspicious_found = True

    if suspicious_found == False:
        print("No suspicious IP addresses found.")

    # Highest risk IP
    print("----------------------")
    print("Highest Risk IP")

    highest_ip = ""
    highest_attempts = 0

    for ip in failed_attempts:

        if failed_attempts[ip] > highest_attempts:
            highest_attempts = failed_attempts[ip]
            highest_ip = ip

    if highest_ip != "":
        print(highest_ip, "with", highest_attempts, "failed attempts.")
    else:
        print("No failed login attempts found.")

    # Security alerts
    print("----------------------")
    print("Security Alerts")

    for ip in failed_attempts:

        if failed_attempts[ip] >= 3:
            print("ALERT:", ip, "has multiple failed login attempts!")

print("====================================")