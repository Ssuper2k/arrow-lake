import plistlib
import os
import shutil

# Path to your config.plist
plist_path = "config.plist"

# Optional: create a backup
backup_path = plist_path + ".backup"
if not os.path.exists(backup_path):
    shutil.copy(plist_path, backup_path)
    print(f"Backup created at {backup_path}")

# Load the plist
with open(plist_path, 'rb') as f:
    plist = plistlib.load(f)

# Navigate to PlatformInfo > Generic
try:
    generic = plist['PlatformInfo']['Generic']
except KeyError:
    print("Could not find PlatformInfo > Generic section.")
    exit(1)

# Clear SMBIOS fields
fields_to_clear = [
    'SystemProductName',
    'SystemSerialNumber',
    'MLB',           # BoardSerialNumber
    'SystemUUID',
    'ROM'            # MAC address or hardware ID
]

for field in fields_to_clear:
    if field in generic:
        generic[field] = ''
        print(f"Cleared {field}")
    else:
        print(f"{field} not found in config.plist")

# Save the modified plist
with open(plist_path, 'wb') as f:
    plistlib.dump(plist, f)

print("SMBIOS info cleared successfully.")

