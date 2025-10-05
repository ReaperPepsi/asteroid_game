from circleshape import *
from constants import *
from shoot import *

class Player(CircleShape):
    def __init__(self, x, y, player_radius):
        super().__init__(x, y, player_radius)
        self.rotation = 0
        self.timer = 0
        self.shots = []

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, color ="white", points= self.triangle(), width=2)
    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if self.timer < 0:
            self.timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0: 
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # 1. Calculate the forward direction vector using the player's rotation
        # This is the key part you've already used in other methods!
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # 2. Create a new Shoot object, passing the correct direction
        new_shot = Shoot(
            x=self.position[0], 
            y=self.position[1], 
            radius=SHOT_RADIUS, 
            direction=forward_vector # Pass the vector here
        )
        
        # 3. Add the new shot to the player's list of shots
        # You'll need to make sure your main game loop updates and draws these shots
        self.shots.append(new_shot)
        
        # 4. Reset the cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN
