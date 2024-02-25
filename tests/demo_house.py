from smarthouse.domain import SmartHouse, Actuator, Sensor
# Importing the necessary classes from smarthouse/domain.py

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(0)

entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
el_meter = Sensor("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "Electricity Meter", "MysticEnergy Innovations", "Volt Watch Elite")
DEMO_HOUSE.register_device(entrance, el_meter)
smart_lock = Actuator("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "Smart Lock", "MythicalTech", "Guardian Lock 7000")
DEMO_HOUSE.register_device(entrance, smart_lock)
# TODO: continue registering the remaining floor, rooms and devices

guest_room_1 = DEMO_HOUSE.register_room(ground_floor, room_size= 8, room_name= 'Guest Room 1')
smart_oven = Actuator("c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "Smart Oven", "IgnisTech Solutions", "Ember Heat 3000")
DEMO_HOUSE.register_device(guest_room_1, smart_oven)


bathroom_1 = DEMO_HOUSE.register_room(ground_floor, room_size= 6.3, room_name= 'Bathroom 1')
humidity_sensor = Sensor("3d87e5c0-8716-4b0b-9c67-087eaaed7b45","Humidity Sensor", "AetherCorp", "Aqua Alert 800")
DEMO_HOUSE.register_device(bathroom_1, humidity_sensor)


livingroom_kitchen = DEMO_HOUSE.register_room(ground_floor, room_size= 39.75, room_name='LivingRoom and Kitchen')
co2_sensor = Sensor("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "CO2 sensor", "ElysianTech", "Smoke Warden 1000")
DEMO_HOUSE.register_device(livingroom_kitchen, co2_sensor)


motion_sensor = Sensor("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "Motion Sensor", "NebulaGuard Innovations", "MoveZ Detect 69", unit="\°C")
DEMO_HOUSE.register_device(livingroom_kitchen, motion_sensor)


heat_pump = Actuator("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Heat Pump", "ElysianTech", "Thermo Smart 6000")
DEMO_HOUSE.register_device(livingroom_kitchen, heat_pump)


garage = DEMO_HOUSE.register_room(ground_floor, room_size= 19, room_name= 'Garage')
auto_garage = Actuator("9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "Automatic Garage Door", "MythicalTech", "Guardian Lock 9000")
DEMO_HOUSE.register_device(garage, auto_garage)


# Andre Etasje "first floor"
first_floor = DEMO_HOUSE.register_floor(1)


hallway = DEMO_HOUSE.register_room(first_floor, room_size = 10, room_name = 'Hallway')


guest_room_2 = DEMO_HOUSE.register_room(first_floor, room_size= 8, room_name= 'Guest room 2')
light = Actuator("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Light Bulp", "Elysian Tech", "Lumina Glow 4000")
DEMO_HOUSE.register_device(guest_room_2, light)


bathroom_2 = DEMO_HOUSE.register_room(first_floor, room_size= 9.25, room_name= 'Bathroom 2')
dehumidifier = Actuator("9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "Dehumidifier", "ArcaneTech Solutions", "Hydra Dry 8000")
DEMO_HOUSE.register_device(bathroom_2, dehumidifier)


office = DEMO_HOUSE.register_room(first_floor, room_size= 11.75, room_name= 'Office')
plug = Actuator("1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "Smart Plug", "MysticEnergy Innovations", "FlowState X")
DEMO_HOUSE.register_device(office, plug)


guest_room_3 = DEMO_HOUSE.register_room(first_floor, room_size=10, room_name= 'Guest room 3')
air_quality = Sensor("7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "Air Quality Sensor", "CelestialSense Technologies", "AeroGuard Pro")
DEMO_HOUSE.register_device(guest_room_3, air_quality)

dressing_room = DEMO_HOUSE.register_room(first_floor, room_size=4, room_name= 'Dressing room')


master_bedroom = DEMO_HOUSE.register_room(first_floor, room_size=17, room_name= 'Master bedroom')
smart_oven = Actuator("8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "Smart Oven", "AetherCorp", "Pheonix HEAT 333")
DEMO_HOUSE.register_device(master_bedroom, smart_oven)

temp_sensor = Sensor("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "Temperature Sensor", "AetherCorp", "SmartTemp 42")
DEMO_HOUSE.register_device(master_bedroom, temp_sensor)





