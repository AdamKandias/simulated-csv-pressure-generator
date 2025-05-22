import csv
import math

# ====== SETTING VARIABLE CONSTANTS ======
team_id = 3121                            # <-- Change your Team ID here
max_altitude = 670                        # <-- Change the maximum altitude in meters here
alt_75_percent = int(0.75 * max_altitude) # <-- 75% From peak calculation
output_filename = f"simulated_pressure_{max_altitude}_{alt_75_percent}.csv"
# =========================================

# Constants for barometric formula
P0 = 101325      # Sea level standard atmospheric pressure, in Pa
T0 = 288.15      # Standard temperature in Kelvin (15°C)
g = 9.80665      # Gravity (m/s²)
M = 0.0289644    # Molar mass of Earth's air (kg/mol)
R = 8.3144598    # Universal gas constant (J/(mol·K))

def pressure_at_altitude(altitude_m):
    """Calculate pressure in Pascals at a given altitude using barometric formula."""
    return P0 * math.exp(- (g * M * altitude_m) / (R * T0))

# Create 94 altitude points (47 up, 1 peak, 46 down) to total 95 rows with header
half_points = 47
ascend = [round(i * (max_altitude / half_points), 2) for i in range(half_points)]
descend = ascend[::-1]
altitudes = ascend + [max_altitude] + descend  # Total 94 data rows

# Write to CSV
with open(output_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Command", "Team ID", "Simp", "Pressure"])  # Header
    for alt in altitudes:
        pressure = pressure_at_altitude(alt)
        writer.writerow(["CMD", team_id, "SIMP", round(pressure)])

print(f"CSV file '{output_filename}' created with 95 rows.")
