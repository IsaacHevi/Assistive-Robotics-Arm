# Copyright 1996-2024 Cyberbotics Ltd.
# Modified by Group 4 - KNUST Computer Engineering
# Assistive Robotic Arm Project - arm_controller.py
#
# Controls:
# - Hold key to keep moving, release to stop (like a game controller)
# - SHIFT+P for automatic pick and place
# - SHIFT+D for demo

from controller import Robot
from controller import Keyboard

robot = Robot()

robot_name = robot.getName()
print('=== Assistive Robotic Arm Controller ===')
print('Name of the robot: ' + robot_name + '\n')

# Init the motors
m1 = robot.getDevice('joint_1')
m2 = robot.getDevice('joint_2')
m3 = robot.getDevice('joint_3')
m4 = robot.getDevice('joint_4')
m5 = robot.getDevice('joint_5')
m6 = robot.getDevice('joint_6')
m7 = robot.getDevice('gripper::left')

motors = [m1, m2, m3, m4, m5, m6, m7]

# Set initial positions
for m in motors:
    m.setPosition(0)
    m.setVelocity(1)

# Track current positions
positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Small step per timestep while key is held
STEP = 0.01

# Joint limits
LIMITS = [
    (-3.05, 3.05),   # joint_1
    (-1.57, 0.64),   # joint_2
    (-1.34, 1.57),   # joint_3
    (-3.05, 3.05),   # joint_4
    (-1.74, 1.74),   # joint_5
    (-3.05, 3.05),   # joint_6
    (0.0, 0.01),     # gripper
]

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))

def move_joint(index, direction):
    positions[index] += direction * STEP
    positions[index] = clamp(positions[index], LIMITS[index][0], LIMITS[index][1])
    motors[index].setPosition(positions[index])

# ── DEMO FUNCTION ──
def demo():
    m1.setVelocity(1)
    m2.setVelocity(1)
    m3.setVelocity(1)

    if robot.step(0) == -1:
        return
    m1.setPosition(1.6)
    m7.setPosition(0.01)
    positions[0] = 1.6
    positions[6] = 0.01

    if robot.step(1500) == -1:
        return
    m1.setPosition(0)
    positions[0] = 0

    if robot.step(1500) == -1:
        return
    m2.setPosition(0.5)
    positions[1] = 0.5

    if robot.step(700) == -1:
        return
    m2.setPosition(0)
    positions[1] = 0

    if robot.step(700) == -1:
        return
    m1.setPosition(-0.5)
    m4.setPosition(1.4)
    positions[0] = -0.5
    positions[3] = 1.4

    if robot.step(1500) == -1:
        return
    m4.setPosition(0)
    positions[3] = 0

    if robot.step(1500) == -1:
        return
    m5.setPosition(-1)
    positions[4] = -1

    if robot.step(700) == -1:
        return
    m5.setPosition(0)
    positions[4] = 0

    if robot.step(1000) == -1:
        return
    m3.setPosition(0)
    m1.setPosition(0)
    positions[2] = 0
    positions[0] = 0

    if robot.step(500) == -1:
        return
    m6.setPosition(1.5)
    positions[5] = 1.5

    if robot.step(1000) == -1:
        return
    m6.setPosition(0)
    positions[5] = 0

    if robot.step(1000) == -1:
        return
    m7.setPosition(0)
    positions[6] = 0

    if robot.step(500) == -1:
        return
    m7.setPosition(0.01)
    positions[6] = 0.01

# ── PICK AND PLACE FUNCTION ──
def pick_place():
    print("--- Starting Pick and Place Sequence ---")
    m1.setVelocity(0.5)
    m2.setVelocity(0.5)
    m3.setVelocity(0.5)

    print("Step 1: Moving arm to object...")
    if robot.step(0) == -1:
        return
    m1.setPosition(1.6)
    m2.setPosition(0.69)
    m7.setPosition(0.01)
    positions[0] = 1.6
    positions[1] = 0.69
    positions[6] = 0.01

    print("Step 2: Lowering arm...")
    if robot.step(4200) == -1:
        return
    m3.setPosition(0.5)
    positions[2] = 0.5

    print("Step 3: Closing gripper - Picking object...")
    if robot.step(1200) == -1:
        return
    m7.setPosition(0)
    positions[6] = 0

    print("Step 4: Lifting object...")
    if robot.step(1500) == -1:
        return
    m3.setPosition(0.3)
    positions[2] = 0.3

    print("Step 5: Moving to drop location...")
    if robot.step(1200) == -1:
        return
    m1.setPosition(0)
    positions[0] = 0

    print("Step 6: Placing object...")
    if robot.step(5000) == -1:
        return
    m3.setPosition(0.5)
    positions[2] = 0.5

    print("Step 7: Opening gripper - Releasing object...")
    if robot.step(500) == -1:
        return
    m7.setPosition(0.01)
    positions[6] = 0.01

    print("Step 8: Returning to home...")
    if robot.step(500) == -1:
        return
    m3.setPosition(0)
    m2.setPosition(0)
    positions[2] = 0
    positions[1] = 0

    for m in motors:
        m.setVelocity(1)

    print("--- Pick and Place Complete! ---")

# ── MAIN LOOP ──
print("============ ASSISTIVE ROBOTIC ARM CONTROLS ============")
print("Joint 1 (Base Rotation)   --> SHIFT+A (left)  SHIFT+Z (right)")
print("Joint 2 (Shoulder)        --> SHIFT+Q (up)    SHIFT+S (down)")
print("Joint 3 (Elbow)           --> SHIFT+W (bend)  SHIFT+X (extend)")
print("Joint 4 (Wrist Roll)      --> SHIFT+Y (left)  SHIFT+U (right)")
print("Joint 5 (Wrist Pitch)     --> SHIFT+H (up)    SHIFT+J (down)")
print("Joint 6 (End Rotation)    --> SHIFT+B (left)  SHIFT+N (right)")
print("Gripper                   --> SHIFT+L (open)  SHIFT+M (close)")
print("Hold key = keep moving. Release = stop.")
print("SHIFT+D = Demo  |  SHIFT+P = Pick and Place")
print("========================================================")

timestep = int(robot.getBasicTimeStep())
keyboard = Keyboard()
keyboard.enable(timestep)

while robot.step(timestep) != -1:

    key = keyboard.getKey()

    if key == Keyboard.SHIFT + ord('A'):
        move_joint(0, -1)

    elif key == Keyboard.SHIFT + ord('Z'):
        move_joint(0, +1)

    elif key == Keyboard.SHIFT + ord('Q'):
        move_joint(1, +1)

    elif key == Keyboard.SHIFT + ord('S'):
        move_joint(1, -1)

    elif key == Keyboard.SHIFT + ord('W'):
        move_joint(2, +1)

    elif key == Keyboard.SHIFT + ord('X'):
        move_joint(2, -1)

    elif key == Keyboard.SHIFT + ord('Y'):
        move_joint(3, +1)

    elif key == Keyboard.SHIFT + ord('U'):
        move_joint(3, -1)

    elif key == Keyboard.SHIFT + ord('H'):
        move_joint(4, +1)

    elif key == Keyboard.SHIFT + ord('J'):
        move_joint(4, -1)

    elif key == Keyboard.SHIFT + ord('B'):
        move_joint(5, +1)

    elif key == Keyboard.SHIFT + ord('N'):
        move_joint(5, -1)

    elif key == Keyboard.SHIFT + ord('L'):
        move_joint(6, +1)

    elif key == Keyboard.SHIFT + ord('M'):
        move_joint(6, -1)

    elif key == Keyboard.SHIFT + ord('D'):
        print("Demonstrator: Move Joints")
        demo()

    elif key == Keyboard.SHIFT + ord('P'):
        print("Demonstrator: Pick And Place")
        pick_place()

    # When no key is pressed, joints hold their last position automaticallyAA