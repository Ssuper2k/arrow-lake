# 💻 EFI for z890 Intel core ultra 9 285k (macOS)

This repository contains a custom OpenCore EFI configuration for running macOS on the **Dell Precision 5550** with the following hardware:

## 🧰 System Specs

- **MOBO**: Asus Hero z890  
- **CPU**: Intel core ultra 285k 
- **GPU**: AMD Radeon 6900XT (16GiB)  
- **SSD**: Samsung 9100 Pro 2TiB Pcie5
- **RAM**: 48GiB (2x24GiB @ 8400MTs) - CU DIMM 
- **Display**: LG Ultragear+ OLED 45" 5k2k (PbP 2x)
- **macOS Version**: Sequoia 15.71  
- **OpenCore Version**: 1.05  

---

## ✅ What Works

- **Network**: *Intel Ethernet I226-V (2.5 Gbit):*
- **Bluetooth 5.0**: *(Asus Dongle AC55BT)*
- **Keyboard Media/Volume controls**
- **Video out:** DP + HDMI + Usb-C
- **All/most USB ports**
- **SLEEP** after resume I loose anlalog sound, though

---

## ⚠️ Important Notes

- **SMBIOS**: Please generate your own SMBIOS data using [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) to avoid iCloud and serial number conflicts.


---

## 📁 Folder Structure

This repo contains the full EFI folder, including:
- `ACPI/`
- `Drivers/`
- `Kexts/`
- `OC/config.plist`

Make sure to mount your EFI partition and replace its contents with this folder.

Actualiza el nombre de tu CPU con:
https://github.com/corpnewt/CPU-Name

Also don't forget to  generate your own SMBIOS data

I used MacPro7,1

More info:

https://www.reddit.com/r/hackintosh/comments/1oggx7l/z890_intel_core_ultra_285k_sequoia_1571/

---

## 🛠️ Credits

Thanks to the Hackintosh community and tools like OpenCore, Dortania guides, and GenSMBIOS.

---

## 📌 Disclaimer

This EFI is provided as-is for educational and testing purposes. Use at your own risk. Always back up your data before making system-level changes.

