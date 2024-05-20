disp("Spherical Manilpulator Forward Kinematics")

syms a1 a2 a3 a4 t1 t2 d3

%% Link Lengths

a1 = 50;
a2 = 20;
a3 = 15;

%% Joint Variables

t1 = pi/180*(0);
t2 = pi/180*(90);
d3 = 25;

%% D-H Parameters: [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0, offset = 0, after offset put the value of theta

H0_1 = Link([0,a1,0,pi/2,0,t1]); 
H0_1.qlim = pi/180*[-180 180];

H1_2 = Link([0,0,0,pi/2,0,t2]);
H1_2.qlim = pi/180*[-45 45];
    
H2_3 = Link([0,0,0,0,1,a2+a3]);
H2_3.qlim = [0 d3];

%% Build Mechanical Manipulator

Spherical = SerialLink([H0_1 H1_2 H2_3], 'name', 'Spherical Pick And Place')
Spherical.plot([0 0 0], 'workspace', [-80 80 -80 80 -10 130])
% Spherical.teach

ti1 = 0:0.5:10
ti2 = 0:0.5:2

q0 = [0 0 0];
q1 = [45*pi/180 -20*pi/180 0];
q2 = [45*pi/180 -20*pi/180 25];
q3 = [45*pi/180 0*pi/180 0];
q4 = [-90*pi/180 -20*pi/180 0];
q5 = [-90*pi/180 -20*pi/180 25];
q6 = [45*pi/180 0*pi/180 0];
q7 = [45*pi/180 -20*pi/180 0];
q8 = [45*pi/180 -20*pi/180 25];
q9 = [45*pi/180 0*pi/180 0];
q10 = [180*pi/180 -20*pi/180 0];
q11 = [180*pi/180 -20*pi/180 25];


Traj1 = jtraj(q0,q1,ti2);
Traj2 = jtraj(q1,q2,ti2);
Traj3 = jtraj(q2,q3,ti1);
Traj4 = jtraj(q3,q4,ti1);
Traj5 = jtraj(q4,q5,ti1);
Traj6 = jtraj(q5,q6,ti2);
Traj7 = jtraj(q6,q7,ti2);
Traj8 = jtraj(q7,q8,ti2);
Traj9 = jtraj(q8,q9,ti1);
Traj10 = jtraj(q9,q10,ti1);
Traj11 = jtraj(q10,q11,ti1);
Traj12 = jtraj(q11,q0,ti2);

syms x1 x2 y1 y2 z1 z2

x1 = -100.0;
x2 = 100.0;
y1 = -100.0;
y2 = 100.0;
z1 = -10;
z2 = 100.0;

plot(Spherical,Traj1,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj2,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj3,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj4,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj5,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj6,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj7,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj8,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj9,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj10,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj11,'workspace', [x1 x2 y1 y2 z1 z2])
plot(Spherical,Traj12,'workspace', [x1 x2 y1 y2 z1 z2])




