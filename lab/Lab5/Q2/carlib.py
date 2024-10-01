class Car:
    def __init__(self, make, model, num_of_door):
        self._make = make
        self._model = model
        self._num_of_door = num_of_door
        self._is_car_running = False
        self._current_trip = []

    # Getters
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_num_of_door(self):
        return self._num_of_door

    def is_car_running(self):
        return self._is_car_running

    # Setters
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_num_of_door(self, num_of_door):
        self._num_of_door = num_of_door

    # Start the engine
    def start_engine(self):
        self._is_car_running = True
        self._current_trip = []

    # Stop the engine
    def stop_engine(self):
        self._is_car_running = False

    # Add motion to current trip
    def add_motion(self, distance_in_m, duration_in_sec):
        if self._is_car_running:
            motion = {"distance_in_m": distance_in_m, "duration_in_sec": duration_in_sec}
            self._current_trip.append(motion)
            # Speed in km/h
            speed = (distance_in_m / 1000) / (duration_in_sec / 3600)
            return speed
        else:
            raise Exception("Engine is not running. Start the engine first.")

    # Compute total travel time in minutes
    def compute_current_trip_travel_time_in_minute(self):
        total_time_sec = sum([motion["duration_in_sec"] for motion in self._current_trip])
        return total_time_sec / 60

    # Compute total distance in kilometers
    def compute_current_trip_total_distance_in_km(self):
        total_distance_m = sum([motion["distance_in_m"] for motion in self._current_trip])
        return total_distance_m / 1000

    # Compute average speed in km/h
    def compute_current_trip_average_speed_in_km_per_hour(self):
        total_distance_km = self.compute_current_trip_total_distance_in_km()
        total_time_hours = self.compute_current_trip_travel_time_in_minute() / 60
        if total_time_hours > 0:
            return total_distance_km / total_time_hours
        else:
            return 0

    # String representation of the Car
    def to_string(self):
        return f"Car(make={self._make}, model={self._model}, num_of_door={self._num_of_door}, is_car_running={self._is_car_running})"
