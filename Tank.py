class Tank:
    def __init__(self,forward_speed,backward_speed,turn_speed,bullet_count,color,x,y,heading,width=10,hight=5,bullet='normal'):
        self.forward_speed = forward_speed
        self.backward_speed = backward_speed
        self.turn_speed = turn_speed
        self.bullet_count = bullet_count

        if color == 'red':
            self.color = (255,0,0)
        elif color == 'green':
            self.color = (0,255,0)
        elif color == 'blue':
            self.color = (0,0,255)
        elif ogcolor == 'yellow':
            self.color = (0,255,255)
        elif color == 'pink':
            self.color = (255,150,150)
        elif self.color == 'orange':
            self.color = (255,160,60) 
        elif color == 'black':
            self.color = (0,0,0)
        elif self.color == 'white':
            self.color = (255,255,255)
        elif color == 'gray':
            self.color = (50,50,50)
        else:
            self.color = color

        self.x = x
        self.y = y
        self.heading = heading
    def move_forward(self,speed = 'd'):
        from math import sin,cos
        if speed == 'd':
            speed = self.forward_speed
            
        vx = speed * cos(self.heading)
        vy = speed * sin(self.heading)
        
        self.x+=vx
        self.y+=vy
    def move_backward(self,speed='d'):
        from math import sin,cos
        if speed == 'd':
            speed = self.backward_speed
            
        vx = -speed * cos(self.heading)
        vy = -speed * sin(self.heading)
        
        self.x+=vx
        self.y+=vy

    def turn_clockwise(self,speed = 'd'):
        if speed == 'd':
            speed = self.turn_speed
            
        self.heading += self.turn_speed

    def turn_counterclockwise(self,speed = 'd'):
        if speed == 'd':
            speed = -self.turn_speed
            
        self.heading += self.turn_speed
    
    
    def powerup(self,pu):
        self.bullet = pu
        
    def fire(self):
        import classBullets
        from math import sin,cos
        
        x = self.x+(self.width)*cos(self.heading)/2
        y = self.y+self.width*sin(self.heading)/2
        
        if bullet == 'normal':
            return classBullets.Bullet(x=x.x,y=y,heading=self.heading)
        elif bullet == 'laser':
            return classBullets.Laser(x=x.x,y=y,heading=self.heading)
        elif bullet == 'spray':
            return classBullets.Bullet(x=x.x,y=y,heading=self.heading,typ='spray')
        elif bullet == 'mortar':
            return classBullets.Mortar(x=x.x,y=y,heading=self.heading)

            




