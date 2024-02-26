class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0 
        self.is_engine_started = False

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        if self.is_engine_started:
            self.current_speed -= self.tyre_friction
            if self.current_speed < 0:
                self.current_speed = 0

    def sound_horn(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            print("Beep Beep")


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is False
    car.start_engine()  # Starting the engine
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is True