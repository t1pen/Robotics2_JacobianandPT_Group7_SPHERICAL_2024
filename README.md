<h1 align="center">Robotics2: Jacobian and Path & Trajectory Planning</h1>
<h2 align="center">Group 7 - Spherical Manipulator - 2024</h2>
<br>

## Table of Contents
  - [I. Abstract](#i-abstract)
  - [II. Introduction](#ii-introduction)
  - [III. Jacobian Matrix](#iii-jacobian-matrix)
  - [IV. Differential Equation](#iv-differential-equation)
  - [V. Path and Trajectory Planning](#v-path-and-trajectory-planning)
  - [VI. References](#vi-references)
  - [VII. Group Members](#x-group-members)
<hr> 
<br>


## I. Abstract
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This final project focuses on the full analysis and implementation of Jacobian matrices for path and trajectory planning in a spherical manipulator. The spherical manipulator, with its three rotational degrees of freedom, presents a unique challenge for kinematic analysis and control. Our study begins with the derivation of the Jacobian matrix, which is critical for understanding the link between joint and end-effector velocities. It is also use to investigate singularities and manipulability, assuring efficient and accurate manipulator control. This core element makes it easier to analyze the manipulator's kinematic behavior and dynamic response. Following that, we concentrate on path planning, which aims to create a viable route for the manipulator's end-effector from a starting point to a destination location in a three-dimensional workspace.  This includes preventing collisions, optimizing the trajectory for efficiency, and adhering to the manipulator's kinematic limitations. Trajectory planning is then handled, and time-parameterized motion profiles are created to assure smooth and continuous traverse along the intended path.
  </p>
<br>


## II. Introduction
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>

## III. Jacobian Matrix
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The <b><i>Jacobian Matrix</i></b> is the matrix that relates the end-effector velocities to joint velocities. It is also a partial derivative of the forward kinematics equation. The Jacobian matrix is a fundamental term in robotics that refers to the kinematics of robotic manipulators. It is essential for understanding and directing the movements of robotic arms. The Jacobian matrix is a mathematical depiction of the link between the velocities of a robot's joints and the velocity of its end-effector (tool or hand). It is a partial derivative matrix that transforms joint velocities into linear and angular velocities for the end-effector.
  </p>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In calculus, we have a different type of velocity
  </p>
<br>


<div align="center">

|  Type of Velocity  | Definition | Formula |
|         :---: |     :-----:      |     :-----:      |
| _Constant Velocity_ |   It is the displacement over time (t). It also implies that the end-effector of the robot moves at a steady rate in a specified direction. |  $$V = \frac{D}{t}$$ |
| _Average Velocity_ |    It is the change in time (t). It helps in evaluating how effectively a robot completes its movements over a given period, ensuring smooth and predictable performance in applications like assembly lines, where consistent timing is essential.  |  $$V = \frac{{D_{2}}-{D_{1}}}{{t_{2}}-{t_{1}}}$$ $$V = \frac{&#8710;D}{&#8710;t}$$ |
| _Instantaneous Velocity_ |    It is the rate of change in displacement with respect to time (t). It describes how quickly and in which direction the end-effector is moving at any given instant.  |  $$V = \frac{dD}{dt}$$ $$V = D&#x2D9;$$ |

</div>
<br>



## IV. Differential Equation
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>


## V. Path and Trajectory Planning
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>


## VI. References
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>


## VII. Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.





