


def length_converter(length, from_unit, to_unit):

    # meters_per_unit_of
    m_per_unit = {
        "mm": 0.001,
        "cm": 0.01,
        "dm": 0.1,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }

    if from_unit not in m_per_unit:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in m_per_unit:
        raise ValueError(f"Unknown to_unit: {to_unit}")

    length_in_m = length * m_per_unit[from_unit] # if 1 unit of km has 1000 meters, then 5 units have 5000 meters.
    return length_in_m / m_per_unit[to_unit]     # if 1 unit of km has 1000 meters, then 5000 meters have 5 units.


def weight_converter(weight, from_unit, to_unit):

    # grams_per_unit_of
    g_per_unit = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.349523125,
        "lb": 453.59237,
    }

    if from_unit not in g_per_unit:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in g_per_unit:
        raise ValueError(f"Unknown to_unit: {to_unit}")

    weight_in_g = weight * g_per_unit[from_unit]
    return weight_in_g / g_per_unit[to_unit]


def temp_converter(temp, from_unit, to_unit):
    # from_unit -> Celsius
    if from_unit == "C":
        celsius = temp
    elif from_unit == "F":
        celsius = (temp - 32) * 5 / 9
    elif from_unit == "K":
        celsius = temp - 273.15
    else:
        raise ValueError(f"Unknown from_unit: {from_unit}")

    # Celsius -> to_unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown to_unit: {to_unit}")
