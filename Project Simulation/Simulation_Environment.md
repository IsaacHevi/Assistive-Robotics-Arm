## Simulation Environment Setup

Creating the Webots Project for our Assistive Robotic Arm
The first step involved creating a new simulation project in Webots.

Steps:
1.	Open Webots.
2.	Select File → New Project Directory.
3.	Create a project folder.
4.	Webots automatically generates the following directories:

assistive_robotic_arm_project/
controllers/
worlds/
protos/
textures/

The main simulation world was saved inside the worlds directory


## Creation of the Simulation World

World Initialization

A new world file was created to represent the simulation environment.

Assistive-Robotics-Arm.wbt

The default nodes included:

•WorldInfo

•Viewpoint

•TexturedBackground

•TexturedBackgroundLight

These nodes define the simulation properties, camera position, and environment lighting.

## Floor Creation

To create a working environment for the robot, a floor node was added.

Procedure
	1.	Open the Scene Tree.
	
  2.	Right-click the root node.
	
  3.	Select Add New Node.
	
  4.	Choose Floor.

Floor Configuration

floorSize = 8 8

tileSize = 0.5 0.5

This creates a 8m × 8m workspace for the robot.

The floor acts as the base surface where all objects and structures are placed.


## Table Workspace Setup

A table was added to serve as the robot’s working surface where objects would be placed and picked.

Steps
1.	Add a Table node or create a custom table using a Box shape.
2.	Set the table position and dimensions.

Configuration

Length: 3.2 m

Width: 2.1 m

Height: 0.75 m

The table height ensures the robotic arm can easily reach the objects.


## Adding Pickable Objects

Objects were added to the table to serve as items the robot would pick and move.

Object Creation Steps
	1.	Add a Solid node.
	2.	Insert a water bottle inside it .

Object dimensions

size = 0.05 0.05 0.05

Object placement

Objects were placed on the table using translation coordinates.


## Enabling Physics for Objects

To allow interaction between the robot and the objects, physics properties were added.

Physics configuration

Physics {
 mass 0.2
}

This allows objects to respond to gravity and be manipulated by the robotic gripper


## Robot Arm with Gripper

A robotic arm equipped with a two-finger gripper was used to perform the pick-and-place operation.

Robot structure

Robot

Base

Arm joints

Wrist

Gripper

Left finger

Right finger

The gripper consists of two fingers controlled by motors that open and close to hold objects.


## Virtual representation of the whole simulation environment
<img width="1115" height="789" alt="Assistive-Robotics-Arm_2" src="https://github.com/user-attachments/assets/4d38f6fd-f896-4df6-9a8f-d184dae8a001" />
<img width="1115" height="789" alt="Assistive-Robotics-Arm_1" src="https://github.com/user-attachments/assets/c02d26a9-377d-418a-9d73-e41dfa94ce25" />
<img width="1115" height="789" alt="Assistive-Robotics-Arm" src="https://github.com/user-attachments/assets/a8141671-5f91-4d59-b2f5-968bf0e5c0cb" />


