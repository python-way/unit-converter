from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return ( 
             """ <form action="/length" method="get">
                    <input type="submit" value="length">
                 </form>
             """ 
            +
             """ <form action="/weight" method="get">
                    <input type="submit" value="weight">
                 </form>
             """ 
            +
             """ <form action="/temp" method="get">
                    <input type="submit" value="temp">
                 </form>
             """ 
            )
@app.route("/length")
def length():
    length = request.args.get("length", "")
    from_unit = request.args.get("from-unit", "")
    to_unit = request.args.get("to-unit", "")
    
    if length and from_unit and to_unit:
        converted_value = length_converter(length, from_unit, to_unit)
    else:
        converted_value = ""
    return (
             """ <form action="/" method="get">
                    <input type="submit" value="home">
                 </form>
             """ 
             +
            """ <form action="" method="get"> 
                <p>Enter the length to convert</p> 
                <input type="text" name="length">
                <p>Unit to convert from</p> 
                <input type="text" name="from-unit">
                <p>Unit to convert to</p> 
                <input type="text" name="to-unit">
                <br/>
                <br/>
                <input type="submit" value="convert">
            </form>""" 
            + 
            "<p> Result of your calculation </p>" + converted_value 
        )

@app.route("/weight")
def weight():
    weight = request.args.get("weight", "")
    from_unit = request.args.get("from-unit", "")
    to_unit = request.args.get("to-unit", "")
     
    if weight and from_unit and to_unit:
        converted_value = weight_converter(weight, from_unit, to_unit)
    else:
        converted_value = ""
    return (
             """ <form action="/" method="get">
                    <input type="submit" value="home">
                 </form>
             """ 
             +
            """ <form action="" method="get"> 
                <p>Enter the weight to convert</p> 
                <input type="text" name="weight">
                <p>Unit to convert from</p> 
                <input type="text" name="from-unit">
                <p>Unit to convert to</p> 
                <input type="text" name="to-unit">
                <br/>
                <br/>
                <input type="submit" value="convert">
            </form>""" 
            + 
            "<p> Result of your calculation </P>" + converted_value 
        )


@app.route("/temp")
def temp():
    temp = request.args.get("temp", "")
    from_unit = request.args.get("from-unit", "")
    to_unit = request.args.get("to-unit", "")
     
    if temp and from_unit and to_unit:
        converted_value = temp_converter(temp, from_unit, to_unit)
    else:
        converted_value = ""
    return (
             """ <form action="/" method="get">
                    <input type="submit" value="home">
                 </form>
             """ 
             +
            """ <form action="" method="get"> 
                <p>Enter the temp to convert</p> 
                <input type="text" name="temp">
                <p>Unit to convert from</p> 
                <input type="text" name="from-unit">
                <p>Unit to convert to</p> 
                <input type="text" name="to-unit">
                <br/>
                <br/>
                <input type="submit" value="convert">
            </form>""" 
            + 
            "<p> Result of your calculation </P>" + converted_value 
        )


   
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

    try:
        length_in_m = float(length) * m_per_unit[from_unit] # if 1 unit of km has 1000 meters, then 5 units have 5000 meters.
        return str(round((length_in_m / m_per_unit[to_unit]), 3))     # if 1 unit of km has 1000 meters, then 5000 meters have 5 units.
    except ValueError:
        return "invalid input" 



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
    
    try:
        weight_in_g = float(weight) * g_per_unit[from_unit]
        return str(round((weight_in_g / g_per_unit[to_unit]), 3))
    except ValueError:
        return "invalid input" 


def temp_converter(temp, from_unit, to_unit):

    try:
        temp = float(temp)
        # from_unit -> Celsius
        if from_unit.lower() == "c":
            celsius = temp
        elif from_unit.lower() == "f":
            celsius = round(((temp - 32) * 5 / 9), 3)
        elif from_unit.lower() == "k":
            celsius = round((temp - 273.15), 3)
        else:
            raise ValueError(f"Unknown from_unit: {from_unit}")

        # Celsius -> to_unit
        if to_unit.lower() == "c":
            return str(celsius)
        elif to_unit.lower() == "f":
            return str(round(celsius * 9 / 5 + 32, 3))
        elif to_unit.lower() == "k":
            return str(round((celsius + 273.15), 3))
        else:
            raise ValueError(f"Unknown to_unit: {to_unit}")

    except ValueError:
        return "invalid input" 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
