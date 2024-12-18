# Ian Gabriel Vista
# Algorithm 2
def find_preferred_starting_city(distances, gas, mpg):
  n = len(distances)
  current_fuel = 0
  potential_starting_city = 0

  for i in range(n):
    current_fuel -= distances[i] / mpg
    current_fuel += gas[i]

    if current_fuel < 0:
      potential_starting_city = (i + 1) % n  # Handle circularity
      current_fuel = 0

  return potential_starting_city

# Sample input
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

preferred_city = find_preferred_starting_city(city_distances, fuel, mpg)
print("Preferred starting city:", preferred_city)