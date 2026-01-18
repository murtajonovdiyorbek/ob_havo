# import asyncio



# async def generate():
#     for i in range(1,11):
#         print(i)
#         await asyncio.sleep(0.0001)
        
        
        
# async def message():
#     for i in range(1,11):
#         print("asinxrom ishladi!!!")
#         await asyncio.sleep(0.0001)
    
    
# async def main():
#     task1 = generate()
#     task2 = message()
#     await asyncio.gather(task1, task2)
    
    
# asyncio.run(main())

#--------------------------------------------------------------------------------------------










import requests
api_key = 'b01e7608c07f15c54ff9d9b64d478705'
city_name = "Oymyakon"


req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")


data = req.json()
print(data)