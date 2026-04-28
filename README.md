# ⚡ Smart Microgrid Monitoring & Control System (ESP32)

A real-time **solar microgrid monitoring and intelligent power switching system** built using ESP32.
This project not only monitors energy but also **automatically manages power flow between solar and battery sources**, just like a real-world microgrid.


---

## 🌟 Key Feature (Core Concept)

### 🔄 Automatic Power Source Switching (Microgrid Logic)

This system is designed to mimic a **real-world smart microgrid**, where energy is managed efficiently between **solar panels and battery storage**.


### ✅ How it Works:

* 🌞 **When Solar Power is Sufficient:**
<img width="573" height="974" alt="WhatsApp Image 2026-04-28 at 9 10 07 PM" src="https://github.com/user-attachments/assets/f132bf84-8fed-4f3a-87d6-fd905f43e705" />

  * Loads are powered directly from **solar energy**
  * Excess energy is **stored in the battery**
  * System operates in **SUNNY mode**

* ☁️ **When Solar Power is Insufficient:**
<img width="575" height="1001" alt="WhatsApp Image 2026-04-28 at 7 34 05 PM" src="https://github.com/user-attachments/assets/2b6c4ce0-3a85-4729-8212-a37823de15ff" />


  * Loads automatically switch to **battery supply**
  * Ensures **uninterrupted power**
  * System operates in **CLOUDY mode**

### 🔁 Result:

* No manual switching required
* Efficient energy usage
* Continuous power supply
* Real microgrid behavior simulation

---

## 🚀 Features

* 🌞 Real-time **solar voltage, current, and power monitoring**
* 🔄 **Automatic switching between Solar & Battery**
* 🔋 **Battery charging when excess solar available**
* 🌡 **Temperature & humidity monitoring**
* 💡 Smart control of **LED & Fan loads**
* 📊 Advanced **live web dashboard**
* 📡 ESP32-based **offline WiFi server**

---

## 🧠 System Overview

This project acts as a **mini smart grid controller**.

### Workflow:

1. Sensors measure:

   * Solar voltage & current
   * Light intensity
   * Temperature & humidity

2. ESP32 calculates:

   * Solar power
   * System efficiency

3. ⚡ **Energy Management System (EMS):**

   * Decides power source (Solar / Battery)
   * Controls relays for load switching
   * Simulates battery charging behavior

4. Dashboard displays everything in real-time


---

## ⚡ Real-World Microgrid Behavior

| Condition     | Power Source   | Battery     |
| ------------- | -------------- | ----------- |
| High sunlight | Solar → Load   | Charging    |
| Low sunlight  | Battery → Load | Discharging |
| Night         | Battery only   | Discharging |

---

## 🔌 Relay-Based Power Switching

Relays act as **automatic source selectors**:

* Switch loads between:

  * Solar supply ☀️
  * Battery supply 🔋

This mimics:

* UPS systems
* Solar hybrid inverters
* Smart grid controllers

---

## 🎯 Why This is Important

This feature makes your project:

* 🔬 More than a monitoring system
* ⚡ A **real energy management system**
* 🏡 Similar to **home solar inverter systems**

---

## 🛠️ Future Improvements

* 🔋 Real battery charging circuit (MPPT)
* ⚡ Automatic load prioritization
* ☁️ IoT cloud monitoring
* 📱 Mobile app control
* 🔌 Grid-tie support

---
