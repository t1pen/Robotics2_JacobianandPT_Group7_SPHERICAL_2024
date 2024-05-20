import roboticstoolbox as rtb
import numpy as np 
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

## Create Spherical Manipulator Model
# link lengths in cm
a1 = float(50)
a2 = float(20)
a3 = float(15)

#link conversion to meters
def cm_to_meter(a):
    m = 100 # 1 meter  = 100 cm
    return a/m

a1 = cm_to_meter(a1)
a2 = cm_to_meter(a2)
a3 = cm_to_meter(a3)

# limit of variable d1
d3 = float(25)
d3 = cm_to_meter(d3)

#Create links
#robot_variable = DHRobot([RevoluteDH(d,r,alpha,offset=theta,qlim)])
#robot_variable = DHRobot([PrismaticDH(d=0,r,alpha,offset=d,qlim)])
Spherical = DHRobot([
    RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    RevoluteDH(0,0,(90.0/180.0)*np.pi,(90.0/180.0)*np.pi,qlim=[-np.pi/4,np.pi/4]),
    PrismaticDH(0,0,(0.0/180)*np.pi,a2+a3,qlim=[0,d3])
], name="Spherical")

print(Spherical)

## Path Trajectory Planning 

# Q Paths (Joint Paths)
# Spherical Joint Variables = ([T1, T2, d3])

# Degrees to Radian
def deg2rad(T):
    return (T/180)*np.pi

q0 = np.array([0,0,0]) # origin

q1 = np.array([deg2rad(float(-45)),
            deg2rad(float(-45)),
            cm_to_meter(float(0))
            ])

q2 = np.array([deg2rad(float(-45)),
            deg2rad(float(-45)),
            cm_to_meter(float(25))
            ])

q3 = np.array([deg2rad(float(-45)),
            deg2rad(float(45)),
            cm_to_meter(float(0))
            ])

q4 = np.array([deg2rad(float(-45)),
            deg2rad(float(45)),
            cm_to_meter(float(25))
            ])
            
q5 = np.array([deg2rad(float(45)),
            deg2rad(float(45)),
            cm_to_meter(float(0))
            ])

q6 = np.array([deg2rad(float(45)),
            deg2rad(float(45)),
            cm_to_meter(float(25))
            ])

q7 = np.array([deg2rad(float(45)),
            deg2rad(float(-45)),
            cm_to_meter(float(0))
            ])

q8 = np.array([deg2rad(float(45)),
            deg2rad(float(-45)),
            cm_to_meter(float(25))
            ])

#Plot Scale
x1 = -0.2
x2 = 1.0
y1 = -1.0
y2 = 1.0
z1 = -0.1
z2 = 1.0

# Trajectory Formula
traj1 = rtb.jtraj(q0,q1,7)
traj2 = rtb.jtraj(q1,q2,5)
traj3 = rtb.jtraj(q2,q3,7)
traj4 = rtb.jtraj(q3,q4,5)
traj5 = rtb.jtraj(q4,q5,7)
traj6 = rtb.jtraj(q5,q6,5)
traj7 = rtb.jtraj(q6,q7,7)
traj8 = rtb.jtraj(q7,q8,5)
traj9 = rtb.jtraj(q8,q0,7)


# plot formula
Spherical.plot(traj1.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj2.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj3.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj4.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj5.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj6.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj7.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj8.q, limits=[x1,x2,y1,y2,z1,z2])
Spherical.plot(traj9.q, limits=[x1,x2,y1,y2,z1,z2], block=True)

