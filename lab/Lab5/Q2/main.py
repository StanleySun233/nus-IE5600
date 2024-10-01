from carlib import Car

# Create a new Car object
my_car = Car(make="Toyota", model="Corolla", num_of_door=4)

# Print initial car details
print(my_car.to_string())  # Toyota, Corolla, 4, False, []

# Start the car engine
my_car.start_engine()

print(my_car.to_string())  # Toyota, Corolla, 4, True, []

# Add motions to simulate the log
speed1 = my_car.add_motion(distance_in_m=300, duration_in_sec=20)  # 0.3 km in 20 sec
print(f"Current motion 300 m 20 sec at speed {speed1:.3f} km/h")

speed2 = my_car.add_motion(distance_in_m=300, duration_in_sec=40)  # 0.3 km in 40 sec
print(f"Current motion 300 m 40 sec at speed {speed2:.3f} km/h")

speed3 = my_car.add_motion(distance_in_m=300, duration_in_sec=60)  # 0.3 km in 60 sec
print(f"Current motion 300 m 60 sec at speed {speed3:.3f} km/h")

speed4 = my_car.add_motion(distance_in_m=1000, duration_in_sec=300)  # 1 km in 300 sec
print(f"Current motion 1000 m 300 sec at speed {speed4:.3f} km/h")

# Stop the car engine
my_car.stop_engine()

# Print the car details including the current trip log
print(my_car.to_string())  # Toyota, Corolla, 4, False, [trip log]

# Calculate and print travel statistics
total_travel_time = my_car.compute_current_trip_travel_time_in_minute()
print(f"Travel Time = {total_travel_time:.3f} min")

total_distance = my_car.compute_current_trip_total_distance_in_km()
print(f"Total Distance = {total_distance:.3f} km")

average_speed = my_car.compute_current_trip_average_speed_in_km_per_hour()
print(f"Average Speed = {average_speed:.3f} km/h")
