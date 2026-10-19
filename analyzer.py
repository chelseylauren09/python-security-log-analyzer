
from collections import Counter

LOG_FILE = "sample_logs.txt"
ALERT_THRESHOLD = 3

failed_ips = Counter()
failed_users = Counter()
total_events = 0
failed_events = 0


try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            total_events += 1

            if "LOGIN_FAILED" in line:
                failed_events += 1

                parts = line.split()
                username = None
                ip_address = None

                for part in parts:
                    if part.startswith("user="):
                        username = part.split("=", 1)[1]
                    elif part.startswith("ip="):
                        ip_address = part.split("=", 1)[1]

                if username:
                    failed_users[username] += 1

                if ip_address:
                    failed_ips[ip_address] += 1

except FileNotFoundError:
    print(f"ERROR: Could not find '{LOG_FILE}'.")
    print("Make sure the log file exists in your project folder.")
    raise SystemExit(1)


print("=== SECURITY LOG ANALYZER ===")
print(f"Total log events: {total_events}")
print(f"Failed login attempts: {failed_events}")

print("\nFailed logins by username:")
for username, count in failed_users.most_common():
    print(f"{username}: {count}")

print("\nFailed logins by IP address:")
for ip_address, count in failed_ips.most_common():
    print(f"{ip_address}: {count}")

print("\n=== SECURITY ALERTS ===")
alerts_found = False

for ip_address, count in failed_ips.most_common():
    if count >= ALERT_THRESHOLD:
        print(
            f"ALERT: {ip_address} had "
            f"{count} failed login attempts!"
        )
        alerts_found = True

if not alerts_found:
    print("No suspicious repeated login attempts detected.")
