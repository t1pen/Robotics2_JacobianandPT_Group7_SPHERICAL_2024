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
  - [VII. Group Members](#vii-group-members)
<hr> 
<br>


## I. Abstract
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This final project focuses on the full analysis and implementation of Jacobian matrices for path and trajectory planning in a spherical manipulator. The spherical manipulator, with its three rotational degrees of freedom, presents a unique challenge for kinematic analysis and control. Our study begins with the derivation of the Jacobian matrix, which is critical for understanding the link between joint and end-effector velocities. It is also use to investigate singularities and manipulability, assuring efficient and accurate manipulator control. This core element makes it easier to analyze the manipulator's kinematic behavior and dynamic response. Following that, we concentrate on path planning, which aims to create a viable route for the manipulator's end-effector from a starting point to a destination location in a three-dimensional workspace.  This includes preventing collisions, optimizing the trajectory for efficiency, and adhering to the manipulator's kinematic limitations. Trajectory planning is then handled, and time-parameterized motion profiles are created to assure smooth and continuous traverse along the intended path. 
  </p>
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Furthermore, the jacobian matrix helps with tasks like obstacle avoidance, path optimization, and trajectory tracking by facilitating motion planning and trajectory development for spherical manipulators. Engineers can use the Jacobian matrix to generate viable and smooth trajectories that will satisfy specific task criteria through the use of numerical techniques and optimization algorithms.
<br>
<br>
  
## II. Introduction
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This project delves into the fascinating world of mechanical manipulators, specifically <b><i>spherical manipulators</i></b> which can perform complex movements within a spherical workspace. The objective of this project is to comprehend the relationship between control, motion planning, and the manipulator's fundamental properties. 

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The project begins with exploring the <b><i>Jacobian Matrix</i></b>, a fundamental tool for connecting the end-effector's movement to the spherical manipulator's joint rotations. We'll look at how this matrix reflects the spherical nature of the workspace, allowing us to precisely control the manipulator's orientation and position. Next, we'll venture into the realm of <b><i>Differential Equations</i></b> and how it becomes a robot or a mechanical manipulator. According to Osorio, Carlos (<i>MathWorks, MATLAB</i>, 2017), We'll use Lagrangian mechanics or Newtonian methods to derive the complex equations that control the manipulator's movements. These equations will take into consideration the joint positions, velocities, and accelerations, as well as manipulator parameters such as link masses and inertia. Because of the spherical design and multiple joints of our manipulator, these equations frequently contain non-linear components, creating a distinct challenge when compared to simpler robots. A critical aspect of the project is understanding <b><i>Singularities</i></b>. These occur when the Jacobian matrix loses its invertibility, essentially taking away a degree-of-freedom from the manipulator. In a spherical manipulator, singularity implies the manipulator loses a degree-of-freedom at a specific configuration, hindering its ability to move in certain directions. We'll explore how careful design and control strategies can prevent the manipulator from reaching these limiting configurations. Finally, we'll delve into <b><i>Path and Trajectory Planning</i></b>. A spherical manipulator's path refers to the sequence of positions its end-effector traces in space, while the trajectory includes both the path and the timing information (velocity and acceleration) associated with that path.  Due to the spherical workspace, planning paths for these manipulators often involves spherical interpolation techniques to ensure smooth and efficient motion within the reachable workspace.

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; By delving into these areas, this project aims to provide a comprehensive understanding of how the Jacobian matrix, differential equations, singularity, and path and trajectory planning work together to orchestrate the intricate movements of a spherical manipulator. This knowledge is crucial for effectively controlling and utilizing these robots in various applications.
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
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>- Linear Velocity</i>: The linear velocity is from the linear displacement, its differential is linear velocity , and this is the linear velocities, the xprime yprime zprime and the d prime. Linear velocity is crucial for understanding and controlling the movement of the robot's end-effector. </p> 
    <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/c3e27cdc8776a10f276b8510a50b4e64434491c0/Robo_finals/441544819_1155781665423847_2642355278148153689_n.png" style="height: 100px;"></p>
</div>
 <br>

<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Carl_Jacobi2.jpg/220px-Carl_Jacobi2.jpg">

<p align="justify"> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Jacobian matrix is named after the eminent German mathematician Carl Gustav Jacob Jacobi, who first developed this important concept in the nineteenth century. Jacobi was a towering figure in the field of mathematics during his time, making substantial contributions to a wide array of mathematical disciplines. His work extended far beyond the Jacobian matrix, impacting areas such as elliptic functions, where he developed fundamental theories that are still in use today.
</p>

<p align="justify"> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In addition, Jacobi made significant strides in the realm of dynamics, where his research provided deeper insights into the behavior of physical systems in motion. His pioneering efforts in differential equations were also groundbreaking, offering new methods and solutions that have been instrumental in the advancement of both pure and applied mathematics.
</p>

<p align="justify">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jacobi's contributions were not limited to theoretical pursuits; he was also known for his work in applied mathematics, where his findings had practical implications for engineering and the physical sciences. His comprehensive approach to mathematical problems and his ability to connect various branches of mathematics demonstrated his profound understanding and innovative thinking.
</p>

<p align="justify">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Overall, Carl Gustav Jacob Jacobi's legacy is a testament to his profound impact on mathematics, with the Jacobian matrix being just one of the many tools and theories that he developed, which continue to influence contemporary mathematical research and applications.
</p>
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


## Methods of Obtaining Jacobian Matrix
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. <i>Partial Derivative Method</i>: The Partial Derivative Method entails directly computing the Jacobian matrix by taking the partial derivatives of the position and orientation functions in relation to the joint variables. </p>
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. <i>Propagation Method</i>: The Propagation Method entails systematically propagating the effects of each joint variable along the robot's kinematic chain to identify their contributions to the end-effector's velocity. </p>
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. <i>Linear Algebra Method</i>: The Linear Algebra Method derives the Jacobian matrix using linear algebra concepts, which frequently include transformation matrices as well as rotation and translation features. </p> 
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.  <i>More</i> </p> 
<br>


### Linear Algebra Method
  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/f79fb09ffc6610c13e84d98d9b0cf22b5be8b7df/Robo_finals/436423704_834066888540735_6153712287409155515_n.png" style="height: 300px;"></p>
</div>
<br>


## Jacobian Matrix of a Spherical Manipulator
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now, let's solve the Jacobian Matrix of a Spherical Manipulator. </p>

  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/aafb450e6b09e5da8a60690ff225642a931b8edd/Robo_finals/Add%20a%20heading%20(2).jpg" style="height: 400px;"></p>
</div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Here is the equation with the Jacobian matrix: </p>
  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/8a6ffd8495482cf43b383ddd42389c9679ab0393/Robo_finals/436403894_1124314095440538_1273832578915125467_n%20(1).png" style="height: 200px;"></p>
  <p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Notice that the q’s were replaced with d’s, which represent “displacement” of the prismatic joint </p>
</div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Next fill in the Jacobian Matrix. remeber that each column represents a single joint. </p>
  <p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/8a6ffd8495482cf43b383ddd42389c9679ab0393/Robo_finals/436403894_1124314095440538_1273832578915125467_n%20(1).png" style="height: 200px;"></p>
  <p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The R in the matrix above stands for "rotation matrix." For instance, $R_{1}^{0}$ represents the rotation matrix from frame 0 to frame 1. </p>
</div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To solve for spherical manipulators, we need to find the rotational matrices for each column. Remeber that any 3x3 matrix that you will multiply to 001 vector, the answer will be the 3rd column of our 3x3 matrix. </p>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $R_{0}^{0}$ means the projection and the reference is 0. So our rotation matrix is an identity matrix. This is the identity matrix of $R_{0}^{0}$: </p>
<br>

<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/8959745f357f735ecc274e399b94c2267e68146f/Robo_finals/436335917_774446098165625_1435850216450301068_n%20(1).png" style="height: 300px;"></p>
  </div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Next is getting the $R_{1}^{0}$.</p>
<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/a27425c0ea1e8b28ea0ab9b1b3a6bc326e0f3578/Robo_finals/441013670_1174567027056400_5702021752363991286_n.png" style="height: 300px;"></p>
  </div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Then  to solve for $R_{2}^{0}$, we will multiply the $R_{1}^{0}$ to $R_{2}^{1}$.</p>
<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/38919bc3f81cd9086731aed2925f94f07a7605c6/Robo_finals/441306171_1192158122154661_7958303080294320935_n.png" style="height: 300px;"></p>
  </div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is the Jacobian Matrix of a Spherical Manipulator.</p>
<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/b34c3999f3a59b839a08067c406253d128e3aa76/Robo_finals/436363130_1033792958168795_7860095000779189097_n.png" style="height: 200px;"></p>
  </div>
<br>


### Jacobian Matrix of a Spherical Manipulator Video Tutorial 
[![Jacobian Matrix of Spherical Manipulator Thumb](https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/assets/157677365/432fe39e-6361-4e30-a8d8-293cf747c4da)](https://youtu.be/TYJMVxX2ZSo)
<br>
<br>


## IV. Differential Equation
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The differential equation of a mechanical manipulator is a mathematical equation that describes the relationship between the manipulator's joint positions, velocities, and accelerations and the forces and torques acting on them.  These equations describe the complex dynamics of the manipulator's motion. Moreover, from the Jacobian Matrix that we have derived, we can obtain the differential equation of the Spherical Manipulator.
  </p>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To obtain the differential equation of a Spherical Manipulator, we will multiply the Jacobian matrix to Joint Velocity Vector.</p>
<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/bb045693a39ec57604705f6b399c8e7d15bb51e7/Robo_finals/441088122_822971186419251_1276723161212912211_n.png" style="height: 200px;"></p>
  </div>
<br>

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is the Differential Equation of a Spherical manipulator</p>
<p align="center">
  <img src="https://github.com/yannaaa23/Testing/blob/ced0d039e2f15f26085546c9eb84ec07424dca4d/Robo_finals/442010576_1128962038417382_9149207397439633798_n.png" style="height: 300px;"></p>
  </div>
<br>


### Differential Equation of a Spherical Manipulator Video Tutorial 
[![Differential Equation of Spherical Manipulator](https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/assets/157677365/6b58fdac-b691-4898-b0db-5145fabae556)](https://youtu.be/D1S0Ut0wUqM?si=_JG4epeChhPKbfvB)

<br>


### Singularities of a Spherical Manipulator Video Tutorial 
[![Singularities of a Spherical Manipulator](https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/main/Images/Singularities%20of%20Spherical%20Manipulator.png)](https://youtu.be/TzwtdPAY8G8?si=PXPP5hhnQi8wAgIj)
<br>


## V. Path and Trajectory Planning
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For a spherical manipulator, <b><i>Path and Trajectory planning</i></b> are critical components of ensuring efficient and precise movements within its spherical workspace. The following descriptions are the breakdown of these concepts:

<p align="justify">
  > <b><i>Path Planning:</b></i> Imagine drawing a line in space; that's essentially what path planning does for a spherical manipulator. It determines the sequence of positions the end-effector will traverse within the reachable sphere. This planning considers factors like obstacles, desired waypoints, and workspace limitations.
  </p>
<p align="justify">
  > <b><i>Trajectory Planning:</b></i> Path planning defines the "where," but trajectory planning adds the "how." It determines the timing information (velocity and acceleration) for the end-effector along the planned path. This ensures the manipulator moves smoothly and efficiently, considering factors like joint limitations, speed constraints, and desired arrival time. Moreover, the trajectory describes how to follow a path as a function of time (Castro, S., <i>MATLAB</i>, 2019).
  </p>
<br>
    
## The Planning Process
<p align="justify">1. <b><i>Task:</b></i> This defines the overall goal, like picking up an object or reaching a specific point. </p>
<p align="justify">2. <b><i>Task Planning:</b></i> from Point A to Point B </p>
<p align="justify">3. <b><i>Path Planning:</b></i> This determines the sequence of positions within the spherical workspace for the end-effector to follow. (figure the set of points) </p>
<p align="justify">4. <b><i>Trajectory Planning:</b></i> This defines the velocity and acceleration profiles for the end-effector along the planned path. </p>
<p align="justify">5. <b><i>Programming:</b></i> This translates the planned trajectory into control signals for the manipulator's joints. </p>
<p align="justify">5. <b><i>Final Output:</b></i> The manipulator executes the planned motion. </p>
<br>

## Path Generation Methods:
<p align="justify">1. <b><i>Joint Space Scheme:</b></i> This method focuses on the joint variables (angles) of the manipulator. It uses functions like <b><i>Cubic Polynomials</b></i>, <b><i>Fifth-Order polynomials</b></i>, or <b><i>Parabolic Blend</b></i> to generate a continuous joint trajectory between start and end configurations. This approach is computationally efficient but may not directly translate to the desired end-effector path in the workspace. </p>
<p align="justify">2. <b><i>Cartesian Scheme: </b></i> This method focuses on the end-effector's position vectors (X, Y, Z) within the workspace. It generates a path directly in Cartesian space, ensuring a more intuitive understanding of the end-effector's movement. However, it may require additional calculations to translate the path into joint commands for the manipulator. </p>
<br>


### Path and Trajectory Planning of a Spherical Manipulator (Forward and Inverse):
<p align="center">
  This is the Forward Path and Trajectory Planning of a Spherical Manipulator
<p align="center">
  <img src="https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/cda09a550d6d482f4e9d2d5d55a25daba9f11cae/GIF/GUI%20PY%20P%26T%20For.gif" style="height: 500px;"></p>
  </div>
<br>

<p align="center">
  This is the Inverse Path and Trajectory Planning of a Spherical Manipulator
<p align="center">
  <img src="https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/cda09a550d6d482f4e9d2d5d55a25daba9f11cae/GIF/GUI%20PY%20P%26T%20Inv.gif" style="height: 500px;"></p>
  </div>
<br>
<br>

<p align="center">
  This is the Path and Trajectory Planning of a Spherical Manipulator for Pick and Place
<p align="center">
  <img src="https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/cda09a550d6d482f4e9d2d5d55a25daba9f11cae/GIF/GUI%20PY%20p%26p.gif" style="height: 500px;"></p>
  </div>
<br>
<br>

<p align="center">
  This is the Path and Trajectory Planning of a Spherical Manipulator for Welding
<p align="center">
  <img src="https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/cda09a550d6d482f4e9d2d5d55a25daba9f11cae/GIF/GUI%20PY%20WELD.gif" style="height: 500px;"></p>
  </div>
<br>
<br>


### Path and Trajectory Planning of a Spherical Manipulator Video Tutorial 
[![Path and Trajectory Planning Vid](https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/928e86977a3166591bddb73449ec7838fb83ca2c/Images/Path%20and%20Trajectory%20of%20Spherical%20Manipulator.png)](https://youtu.be/k2QA0MXXu90)
<br>
<br>

### Path and Trajectory Planning (GUI Calculator) of a Spherical Manipulator Video Tutorial
[![Path and Trajectory Planning Using GUI Vid](https://github.com/t1pen/Robotics2_JacobianandPT_Group7_SPHERICAL_2024/blob/102ad6986ea0d2cc8e525bab4c5237fc1a80beb3/Images/Path%20and%20Trajectory%20(GUI)%20of%20Spherical%20Manipulator.png)](https://youtu.be/9wl5kE7-EJ8)
<br>
<br>

## VI. References
  - https://automaticaddison.com/the-ultimate-guide-to-jacobian-matrices-for-robotics/
- https://www.researchgate.net/profile/Mohamed_Mourad_Lafifi/post/how_to_calculate_the_angular_velocity_of_end_effector_of_two_link_robot_arm/attachment/59d6487c79197b80779a326a/AS%3A467097353494530%401488376095328/download/METR4202+-+Robotics+Tutorial+4+%E2%80%93+Week+4_+Solutions.pdf
- https://mathshistory.st-andrews.ac.uk/Biographies/Jacobi/
- https://www.rosroboticslearning.com/jacobian
- https://www.youtube.com/watch?v=h2YM0CDzDl4&t=647s

<br>


## VII. Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.


