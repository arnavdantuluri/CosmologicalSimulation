import math as m
import random
# from numba import njit, float32, float64
# from numba.experimental import jitclass


# specs = [
#     ('x', float32),
#     ('y', float32),
#     ('mass', float32),
#     ('vX', float32),
#     ('vY', float32),
#     ('density', float32),
#     ('mass_mul', float32),
#     ('G', float32),
#     ('dT', float32),
#     ('deltaX', float32),
#     ('deltaY', float32),
#     ('calculation_speed', float32),
#     ('radius', float64),
#     ('time_step', float32),
#     ('EPSILON', float32)

# ]


class Particle():
    def __init__(self, x, y, vX, vY, mass, density):
        self.x = x
        self.y = y
        self.mass = mass
        self.vX = vX
        self.vY = vY
        self.density = density #default value to calculate particle radius if not utilizing the trig method of calculating values
        self.mass_mul = 200
        self.G = 2 #can be any value placeholder no real need unless using grav_calc_with_trig
        self.dT = 5e4 #Some constant change in time to calclate change in velocity by multiplying change in time with the derivative of velocity or the acceleration
        self.deltaX = 0
        self.deltaY = 0
        self.calculation_speed = 1
        self.radius = self.get_radius()
        self.time_step = 0.025
        self.EPSILON = 0.05


    def get_velocity(self):
        self.velocity = m.sqrt(
            self.x**2+
            self.y**2)

        return self.velocity



    def get_momentum(self):
        self.velocity = self.get_velocity()
        self.momentum = self.velocity * self.mass

        return self.momentum



#need to jit
    def get_radius(self):
        self.radius = (self.mass*self.density*self.mass_mul) / (4/3*m.pi)
        self.radius = self.radius ** (1/3)


        return self.radius


#need to jit
    def get_dist(self, other):
        self.radius = self.get_radius()
        self.distance = m.sqrt(
            (self.x - other.x )**2 +
            (self.y - other.y) ** 2
        )


        return self.distance




    def check_body(self, other):
        if (self.x - other.x != 0) and (self.y - other.y != 0):
            self.velocity = self.get_velocity()
            self.momentum = self.get_momentum()
            self.radius = self.get_radius()
            self.distance = self.get_dist(other)
            return self.velocity, self.momentum, self.radius, self.distance
        else:
            pass


    def calc_force(self, other):
        self.velocity, self.momentum, self.radius, self.distance = self.check_body(other)
        self.force = (self.G*self.mass*other.mass)/(self.distance**2)
        return self.force



    def calc_acc(self, other):
        self.force = self.calc_force(other)
        self.acceleration = self.force/self.mass
        return self.acceleration




    #Update position based on velocity and update velocity based on acceleration used if not calculating using trig 
    def update(self, other):
        self.velocity, self.momentum, self.radius, self.distance = self.check_body(other)
        self.acceleration = self.calc_acc(other)
        self.velocity += self.acceleration * self.dT #calculate change in velocity and add that to the velocity
        self.x += self.velocity * self.dT #calculate change in distance and add that to the x-values and y-values respectively
        self.y += self.velocity * self.dT
        return self.x, self.y, self.velocity



    # def calc_with_trig(self, other):
    #     self.dx = other.x - self.x
    #     self.dy = other.y - self.y


    #     self.r = m.sqrt(self.dx**2 + self.dy**2)

    #     self.F = (self.G * self.mass * other.mass) / self.r**2

    #     self.theta = m.atan2(self.dy, self.dx)

    #     self.Fx += m.cos(self.theta) * self.F
    #     self.Fy += m.sin(self.theta) * self.F

    #     # if self.x or self.y == 900:
    #     #     self.Fx = -self.Fx
    #     #     self.Fy = -self.Fy

    #     self.ax = self.Fx / self.mass
    #     self.ay = self.Fy / self.mass

    #     self.vX += self.ax * self.dT
    #     self.vY += self.ay * self.dT

    #     self.sx = self.vX * self.dT - 0.5 * self.ax * self.dT**2
    #     self.sy = self.vY * self.dT - 0.5 * self.ay * self.dT**2

    #     self.x += self.sx
    #     self.y += self.sy

    #     # if (self.x - other.x == 0) and (self.y - other.y == 0):
    #     #     self.r = (self.r**2 + other.r**2)**(1/2)
    #     #     del other



    #     return self.x, self.y



#need to jit
    def calculateObjectForce(self, other):
        if(self != other):
            self.distance = self.get_dist(other)
            self.radius = self.get_radius()
            self.angleToMass = m.atan2(
                other.y - self.y,
                other.x - self.x
            )

            #Newtonian Formula for x
            self.deltaX += (
 							m.cos(self.angleToMass) *
 							(other.mass/m.pow(self.distance,2))
            )


            #Newtonian formul for y
            self.deltaY += (
 							m.sin(self.angleToMass) *
 							(other.mass/m.pow(self.distance,2))
 			)

            return self.deltaX, self.deltaY


#need to jit
    def applyObjectForce(self, other):

        self.deltaX, self.deltaY = self.calculateObjectForce(other)

        if self.distance < self.radius + other.radius or self.x == 776 or self.x == 0 or self.y == 776 or self.y == 0:
            #handle elastic collision
            self.deltaX = 0
            self.deltaY = 0


        #Integration :)
        self.vX += self.deltaX * self.calculation_speed * self.time_step
        self.vY += self.deltaY * self.calculation_speed * self.time_step

        

        #Integration :)
        self.x += self.vX * self.calculation_speed 
        self.y += self.vY * self.calculation_speed 
		
        self.deltaX = 0
        self.deltaY = 0

        


        return self.x, self.y





    def _main(self, other):
        self.x, self.y = self.applyObjectForce(other)
        return self.x, self.y
        




    
