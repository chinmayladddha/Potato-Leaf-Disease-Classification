from fastapi import FastAPI
from enum import Enum
app=FastAPI()
#@app.get("/hello/{name}")
#async def hello(name):
#    return f"welcome to FastApi Practice {name}"
class AvailableCuisines(str,Enum):
    indian="indian"
    american="american"
    italian="italian"
    chinese="chinese"
    
food_items={'indian':["Samosa","Dosa","Daal Bati"],
            'american':["Hot Dog","Apple Pie"],
            'italian':["Revioli","Pizza"],
            'chinese':["Dim sum","Dumplings"]
            }
#valid_cuisines=food.items.keys()
@app.get("/get_fooditems/{cuisine}")
async def get_fooditems(cuisine:AvailableCuisines):
    return food_items.get(cuisine)

coupon_code={1:'10%',2:'20%',3:'30%'}
@app.get("/get_coupon/{code}")
async def get_items(code:int):
    return{'discount_amount':coupon_code.get(code)}
