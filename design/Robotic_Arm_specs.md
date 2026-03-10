# Robotic Arm Design Specifications
**Project:** Assistive Robotic Arm for People with Limited Mobility  
**Group 4** | Mohammed Ahmed | Asare Kingsley Donkor | Hevi Isaac  
**Supervisor:** Dr. Griffith Selorm Klogo  

---

## 1. Degrees of Freedom (DOF) Design

The arm has 6 Degrees of Freedom. Each joint is driven by one MG996R servo motor.

| Joint | Name | Movement | Direction | Angle Range | Arduino Pin |
|---|---|---|---|---|---|
| J1 | Base Rotation | Rotational | Left / Right | 0° – 180° | D3 |
| J2 | Shoulder | Rotational | Up / Down | 0° – 180° | D5 |
| J3 | Elbow | Rotational | Bend / Extend | 0° – 180° | D6 |
| J4 | Wrist Pitch | Rotational | Up / Down | 0° – 180° | D9 |
| J5 | Wrist Roll | Rotational | Twist / Rotate | 0° – 180° | D10 |
| J6 | Gripper | Linear | Open / Close | 0° – 90° | D11 |

**Total: 6-DOF**

---

## 2. Robotic Arm Dimension Plan

3D Model File: Robotic_Arm_3D_Model_v4.stl | Material: 3D Printed PLA

### Overall Dimensions
| Dimension | mm | cm |
|---|---|---|
| Length (X) | 133.81 mm | 13.38 cm |
| Width (Y) | 259.27 mm | 25.93 cm |
| Height (Z) | 236.09 mm | 23.61 cm |
| Max Reach | ~350 mm | ~35 cm |
| Base Diameter | ~130 mm | ~13 cm |
| Max Payload | ~500 g | 0.5 kg |

### Component Dimensions
| Component | Length | Width | Height |
|---|---|---|---|
| Base Platform | 130 mm | 130 mm | 30 mm |
| Shoulder Link | 40 mm | 30 mm | 50 mm |
| Lower Arm | 120 mm | 25 mm | 25 mm |
| Elbow Joint | 35 mm | 30 mm | 40 mm |
| Upper Arm | 100 mm | 25 mm | 25 mm |
| Wrist Assembly | 50 mm | 30 mm | 35 mm |
| Gripper (closed) | 80 mm | 30 mm | 40 mm |
| Gripper (open) | 80 mm | 60 mm | 40 mm |
<img width="229" height="257" alt="arm_front" src="https://github.com/user-attachments/assets/f2352e9f-cdbe-42de-98b8-1ece678dc8ca" />
<img width="258" height="226" alt="arm_side" src="https://github.com/user-attachments/assets/21a4ce08-bfb3-44f0-bd4d-bdaa9f678786" />
<img width="283" height="287" alt="arm_isometric" src="https://github.com/user-attachments/assets/514d45e6-88fc-4f33-8f84-5d7561874d67" />

---

## 3. Gripper Design

**Type:** Two-Finger Parallel Claw  
**Motor:** MG996R Servo (J6) controlled via Arduino D11  
**Max Opening:** ~60 mm  
**Max Payload:** ~500 g  
**Material:** 3D Printed PLA  
<img width="283" height="287" alt="arm_isometric" src="https://github.com/user-attachments/assets/4bd57177-5dd7-44dd-8179-8ce85fd1060d" />

### How It Works
- User says "Close" or presses joystick button
- Arduino rotates J6 to 0° — fingers close and grip object
- User says "Open" or presses joystick button again  
- Arduino rotates J6 to 90° — fingers open and release object

### Diagram
```
OPEN (90°):          CLOSED (0°):
|          |              ||  ||
|          |              ||  ||
 \        /                \  /
  [SERVO J6]            [SERVO J6]
```
