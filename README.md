# 🌙 Raspberry Pi Pico W – LED Fade using PWM (MicroPython)

This project creates a **breathing light effect** by smoothly increasing and decreasing an LED’s brightness using **PWM (Pulse Width Modulation)** on the **Raspberry Pi Pico W**.

---

## ⚙️ How It Works
PWM (Pulse Width Modulation) controls how long a signal stays HIGH in each cycle — called the **duty cycle**.  
By adjusting this duty cycle between 0% and 100%, we simulate analog brightness on a digital pin.

The code below fades an LED **from dark → bright → dark** in an infinite loop.

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Raspberry Pi Pico W | 1 | Microcontroller board |
| LED | 1 | Any color |
| 220Ω Resistor | 1 | Limits LED current |
| Breadboard & Jumper Wires | - | For connection |

---

## 🧠 Circuit Connection

| LED Pin | Pico W Pin | Description |
|----------|-------------|-------------|
| Anode (+) | GPIO17 | PWM output |
| Cathode (–) | GND | Ground |

💡 Use a resistor (~220Ω) in series to protect your LED.

---
