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
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This project delves into the fascinating world of mechanical manipulators, specifically <b><i>spherical manipulators</i></b> which can perform complex movements within a spherical workspace. The objective of this project is to comprehend the relationship between control, motion planning, and the manipulator's fundamental properties.
  </p>
<br>

## III. Jacobian Matrix
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The <b><i>Jacobian Matrix</i></b> is the matrix that relates the end-effector velocities to joint velocities. It is also a partial derivative of the forward kinematics equation. The Jacobian matrix is a fundamental term in robotics that refers to the kinematics of robotic manipulators. It is essential for understanding and directing the movements of robotic arms. The Jacobian matrix is a mathematical depiction of the link between the velocities of a robot's joints and the velocity of its end-effector (tool or hand). It is a partial derivative matrix that transforms joint velocities into linear and angular velocities for the end-effector.
  </p>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The following are the different type of velocity in Calculus:
  </p>


<div align="center">

|  Type of Velocity  | Definition | Formula |
|         :---: |     :-----:      |     :-----:      |
| _Constant Velocity_ |   It is the displacement over time (t). It also implies that the end-effector of the robot moves at a steady rate in a specified direction. |  $$V = \frac{D}{t}$$ |
| _Average Velocity_ |    It is the change in time (t). It helps in evaluating how effectively a robot completes its movements over a given period, ensuring smooth and predictable performance in applications like assembly lines, where consistent timing is essential.  |  $$V = \frac{{D_{2}}-{D_{1}}}{{t_{2}}-{t_{1}}}$$ $$V = \frac{&#8710;D}{&#8710;t}$$ |
| _Instantaneous Velocity_ |    It is the rate of change in displacement with respect to time (t). It describes how quickly and in which direction the end-effector is moving at any given instant.  |  $$V = \frac{dD}{dt}$$ $$V = D&#x2D9;$$ |

</div>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>Jacobian Matrix</i></b>, particularly in robotics and kinematics, the instantaneous velocity is a key concept. The Jacobian matrix relates the velocities of the joints of a robotic manipulator (or a similar mechanical system) to the velocities of the end effector.
  </p>
<br>


**Type of Instantaneous Velocity:**
<p align="justify"> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>- Angular Velocity</i>: The angular velocity is from the displacement due to rotation, its differential is angular velocity, then we will write it as theta prime. Angular velocity is particularly relevant for rotary joints and rotating end-effectors. 
    <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/967290615783731ff45b7a282223e7c31028e21c/441436226_1195944951572857_5490576830621742157_n.png" style="height: 100px;"></p>
</div>

<p align="justify"> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>- Linear Velocity</i>: The linear velocity is from the linear displacement, its differential is linear velocity , and this is the linear velocities, the xprime yprime zprime and the d prime. Linear velocity is crucial for understanding and controlling the movement of the robot's end-effector. 
    <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/c3e27cdc8776a10f276b8510a50b4e64434491c0/Robo_finals/441544819_1155781665423847_2642355278148153689_n.png" style="height: 100px;"></p>
</div>
 <br>

<p align="justify"> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Jacobian matrix is named after the German mathematician <b><i>Carl Gustav Jacob Jacobi</i></b>, who first developed it in the nineteenth century. Carl Gustav Jacob Jacobi was a well-known mathematician who made significant contributions to several topics, including elliptic functions, dynamics, and differential equations.
<br>
<br>


## Methods of Obtaining Jacobian Matrix
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. <i>Partial Derivative Method</i>: The Partial Derivative Method entails directly computing the Jacobian matrix by taking the partial derivatives of the position and orientation functions in relation to the joint variables. </p>
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. <i>Propagation Method</i>: The Propagation Method entails systematically propagating the effects of each joint variable along the robot's kinematic chain to identify their contributions to the end-effector's velocity. </p>
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. <i>Linear Algebra Method</i>: The Linear Algebra Method derives the Jacobian matrix using linear algebra concepts, which frequently include transformation matrices as well as rotation and translation features. </p> 
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.  <i>More</i> </p> 
<br>


## Overview of the Jacobian Matrix
<p align="justify"> For a three-dimensional robot, the Jacobian matrix converts joint velocities into end effector velocities using the equation below: </p>

   - **q prime** or **q with the dot on top** represents the **joint velocities**.
   - **J** is the **Jacobian matrix**.
   - The left matrix represents the **end effector's velocities**. 
   - **$\dot x$** **$\dot y$** and **$\dot z$** signify **linear velocities**, it is how fast the end effector moves in the x, y, and z directions relative to the base frame of a robotic arm.
   - **$\omega x$** **$\omega y$** and **$\omega z$** are the **angular velocities** of a robotic arm's end effector.

  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/aa89d9d1ecbd6c443e4a55e4fe92338f96ed0a69/Robo_finals/436365194_1125427155179916_2755642066726289969_n.png" style="height: 200px;"></p>
</div>
<br>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The dimension of the Jacobian matrix is composed of rows and columns, the number of rows depends on the number of rows of the end effector velocity vector and the column of the velocity vector is always 6. Then for the column in the jacobian matrix is equal to the number of rows in DH Parametric table. </p>

  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/b7feb726b75d0b2628d83caed946dfd5686e4cb7/Robo_finals/436600182_982208450205345_7391698240201526907_n.png" style="height: 200px;"></p>
</div>
<br>
<br>





## Jacobian Matrix of a Spherical Manipulator
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now, let's solve the Jacobian Matrix of a Spherical Manipulator. </p>

  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/aafb450e6b09e5da8a60690ff225642a931b8edd/Robo_finals/Add%20a%20heading%20(2).jpg" style="height: 400px;"></p>
</div>
<br>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Here is the equation with the Jacobian matrix: </p>




### Jacobian Matrix of a Spherical Manipulator Video Tutorial 

[![picture-link](youtube-link)

<br>



## IV. Differential Equation
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>



### Differential Equation of a Spherical Manipulator Video Tutorial 

[![picture-link](youtube-link)

<br>



## V. Path and Trajectory Planning
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </p>
<br>



### Path and Trajectory Planning of a Spherical Manipulator Video Tutorial 

[![picture-link](youtube-link)

<br>



## VI. References
  - https://automaticaddison.com/the-ultimate-guide-to-jacobian-matrices-for-robotics/

<br>


## VII. Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.


Dot sa taas - $\dot x$
$$\dot \theta$$
$$\omega x$$


