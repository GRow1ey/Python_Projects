weight = float(41.5)

def ground_cost(weight):
  """
  Calculate the ground shipping cost for an item of a particular weight.
  """
  if weight <= 2:
    return weight * 1.50 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3.00 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4.00 + 20
  elif weight > 10:
    return weight * 4.75 + 20

def drone_shipping(weight):
  """
  Calculate the drone shipping cost for an item of a particular weight.
  """
  if weight <= 2:
    return weight * 4.5
  elif weight > 2 and weight <= 6:
    return weight * 9.00
  elif weight > 6 and weight <= 10:
    return weight * 12.00
  elif weight > 10:
    return weight * 14.25

# Ground cost
ground_cost = ground_cost(weight)
print("Ground shipping: $", ground_cost)

# Ground premium cost
ground_premium_cost = 125.0
print("Ground premium shipping: $", ground_premium_cost)

# Drone Shipping
drone_shipping = drone_shipping(weight)
print("Drone shipping: $", drone_shipping)