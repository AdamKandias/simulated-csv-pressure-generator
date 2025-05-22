# Simulated Atmospheric Pressure Generator

This project generates a simulated CSV dataset representing atmospheric pressure changes with respect to altitude using the barometric formula. It is particularly useful for aerospace, CanSat, balloon telemetry simulation, or any educational physics-related project where mock atmospheric data is required.

The output file will automatically be named based on the `max_altitude` and its 75% value, e.g., `simulated_pressure_670_502.csv`.

---

## 🔧 Features

- Simulates atmospheric pressure from ground level up to a defined maximum altitude.
- Supports customization of simulation parameters such as team ID and altitude.
- Outputs **95 rows of data**: 47 ascending, 1 peak, and 47 descending values.
- Follows the standard barometric pressure formula using physical constants.
- Outputs CSV file compatible with GCS systems, telemetry parsers, and data loggers.

---

## ⚙️ Configuration

All key variables are located at the top of the script and are easy to configure:

| Variable         | Default | Description                                                               |
|------------------|---------|---------------------------------------------------------------------------|
| `team_id`        | `3121`  | Your team or mission ID. This will be written in each row of the CSV.     |
| `max_altitude`   | `670`   | The maximum altitude to simulate (in meters). Change this to your target. |
| `alt_75_percent` | Auto    | Automatically calculated as 75% of max_altitude. Used in output filename. |

You can modify these values directly in the script before execution.

---

## 📄 Output File Format

The output file is a `.csv` with the following format:

```
Command,Team ID,Simp,Pressure
CMD,3121,SIMP,101325
CMD,3121,SIMP,100562
...
```

- **Command**: A placeholder command label (e.g., for parsing in a GCS system).
- **Team ID**: Taken from the `team_id` constant.
- **Simp**: Static tag used to indicate this is simulated pressure.
- **Pressure**: Simulated pressure value in Pascals, rounded to the nearest integer.

---

## 📁 File Output Naming Convention

The output CSV will be named dynamically based on the altitude settings:

```
simulated_pressure_<max_altitude>_<75%_altitude>.csv
```

For example, if `max_altitude = 670`, the file will be:

```
simulated_pressure_670_502.csv
```

This helps clearly track the configuration used in each simulation.

---

## ▶️ How to Use

### Prerequisites

- Python 3.x installed
- No additional libraries required (uses built-in modules only)

### To Run:

```bash
python simulated_pressure_generator.py
```

After running the script, you will see:

```
CSV file 'simulated_pressure_670_502.csv' created with 95 rows.
```

---

## 🧪 Algorithm Details

The pressure is calculated using the following barometric formula:

```
P = P0 * exp(-(g * M * h) / (R * T0))
```

Where:

- **P0**: 101325 Pa (sea level pressure)  
- **T0**: 288.15 K (standard temperature)  
- **g**: 9.80665 m/s² (gravitational acceleration)  
- **M**: 0.0289644 kg/mol (molar mass of air)  
- **R**: 8.3144598 J/(mol·K) (universal gas constant)  
- **h**: Altitude in meters  

This provides an exponential decay of pressure with altitude increase.

---

## 🗂️ Folder Structure

```
/simulated_pressure_generator.py
/simulated_pressure_670_502.csv
/README.md
```

---

## 📜 License

MIT License

```
MIT License

Copyright (c) 2025 Adam Kandias
```

---

## 🙋‍♂️ Contact

For any questions, suggestions, or collaborations, feel free to reach out via GitHub Issues or email.
