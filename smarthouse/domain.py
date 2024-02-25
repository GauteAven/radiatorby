from random import randint
from time import time, ctime


class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


# TODO: Add your own classes here!


class Room:
    def __init__(self, room_size, room_name):
        self.device_dict = dict()
        self.devices = []
        self.room_size = room_size
        self.room_name = room_name

    def __str__(self):
        content = ',  '.join([device.__str__() for device in self.devices])
        string = '{a}:\n{b}'.format(a=self.room_name, b=content)
        return string

    def get_area(self):
        return self.room_size

    def register_device(self, device):
        self.device_dict[device.id] = device
        self.devices.append(device)


class Floor:
    def __init__(self, level):
        self.level = level
        self.rooms = []

    def __str__(self):
        content = '\n\n'.join([room.__str__() for room in self.rooms])
        underline = '-'*5
        string = '\n\n{a}:\n{b}\n\n{c}'.format(a=self.level, b=underline, c=content)
        return string

    def get_level(self):
        return self.level

    def register_room(self, room):
        self.rooms.append(room)

    def get_area(self):
        summ = 0
        for room in self.rooms:
            summ += room.get_area()
        return summ


class Device:

    def __init__(self, id, device_type, supplier, model_name, room=None):
        self.id = id
        self.device_type = device_type
        self.supplier = supplier
        self.model_name = model_name
        self.room = room

    def __str__(self):
        string = '{a} (location: {b})'.format(a=self.model_name, b=self.room.room_name)
        return string

    def is_actuator(self):
        return False

    def is_sensor(self):
        return False

    def get_device_type(self):
        return self.device_type

    def register_room(self, room):
        self.room = room


class Actuator(Device):

    def __init__(self, id, device_type, supplier, model_name, room=None):
        super().__init__(id, device_type, supplier, model_name, room)
        self.state = False

    def turn_on(self, target_value=None):
        if not target_value:
            self.state = True
        else:
            self.state = target_value

    def turn_off(self):
        self.state = False

    def is_active(self):
        return self.state

    def is_actuator(self):
        return True


class Sensor(Device):

    def __init__(self, id, device_type, supplier, model_name, room=None, unit="°C"):
        super().__init__(id, device_type, supplier, model_name, room)
        self.unit = unit
        timestamp, value = self.anus()
        self.state = Measurement(timestamp, value, self.unit)

    @staticmethod
    def anus():
        timestamp = ctime(time())
        value = randint(190, 230) / 10
        return timestamp, value

    def is_sensor(self):
        return True

    def last_measurement(self):
        return self.state


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def __init__(self):
        self.floors = []
        self.rooms = []
        self.devices = []

    def __str__(self):
        string = ''.join([floor.__str__() for floor in self.floors])
        return string

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        floor = Floor(level)
        if level > len(self.floors):
            self.floors.append(floor)
        self.floors.insert(level, floor)
        return floor

    def register_room(self, floor, room_size, room_name=None):
        """
        This methods registers a new room with the given room areal size
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        room = Room(room_size, room_name)
        floor.register_room(room)
        self.rooms.append(room)
        return room

    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has
        registered a basement (level=0), a ground floor (level=1) and a first floor
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return self.floors

    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        return self.rooms

    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        summ = 0
        for floor in self.floors:
            summ += floor.get_area()
        return summ

    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        if device not in self.devices:
            self.devices.append(device)
        if device.room and device.room != room and device in device.room.devices:
            location = device.room
            location.devices.remove(device)
            del location.device_dict[device.id]
        device.register_room(room)
        room.register_device(device)

    def get_devices(self):
        return self.devices

    def get_device_by_id(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        for room in self.rooms:
            if device_id not in room.device_dict:
                continue
            return room.device_dict[device_id]


if __name__ == '__main__':
    DEMO_HOUSE = SmartHouse()

    # Building house structure
    ground_floor = DEMO_HOUSE.register_floor(0)

    entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
    el_meter = Sensor("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "Electricity Meter", "MysticEnergy Innovations",
                      "Volt Watch Elite")
    DEMO_HOUSE.register_device(entrance, el_meter)
    smart_lock = Actuator("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "Smart Lock", "MythicalTech", "Guardian Lock 7000")
    DEMO_HOUSE.register_device(entrance, smart_lock)
    # TODO: continue registering the remaining floor, rooms and devices

    guest_room_1 = DEMO_HOUSE.register_room(ground_floor, room_size=8, room_name='Guest Room 1')
    smart_oven = Actuator("c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "Smart Oven", "IgnisTech Solutions",
                          "Ember Heat 3000")
    DEMO_HOUSE.register_device(guest_room_1, smart_oven)

    bathroom_1 = DEMO_HOUSE.register_room(ground_floor, room_size=6.3, room_name='Bathroom 1')
    humidity_sensor = Sensor("3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "Humidity Sensor", "AetherCorp", "Aqua Alert 800")
    DEMO_HOUSE.register_device(bathroom_1, humidity_sensor)

    livingroom_kitchen = DEMO_HOUSE.register_room(ground_floor, room_size=39.75, room_name='LivingRoom and Kitchen')
    co2_sensor = Sensor("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "CO2 sensor", "ElysianTech", "Smoke Warden 1000")
    DEMO_HOUSE.register_device(livingroom_kitchen, co2_sensor)

    motion_sensor = Sensor("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "Motion Sensor", "NebulaGuard Innovations",
                           "MoveZ Detect 69", unit="\°C")
    DEMO_HOUSE.register_device(livingroom_kitchen, motion_sensor)

    heat_pump = Actuator("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Heat Pump", "ElysianTech", "Thermo Smart 6000")
    DEMO_HOUSE.register_device(livingroom_kitchen, heat_pump)

    garage = DEMO_HOUSE.register_room(ground_floor, room_size=19, room_name='Garage')
    auto_garage = Actuator("9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "Automatic Garage Door", "MythicalTech",
                           "Guardian Lock 9000")
    DEMO_HOUSE.register_device(garage, auto_garage)

    # Andre Etasje "first floor"
    first_floor = DEMO_HOUSE.register_floor(1)

    hallway = DEMO_HOUSE.register_room(first_floor, room_size=10, room_name='Hallway')

    guest_room_2 = DEMO_HOUSE.register_room(first_floor, room_size=8, room_name='Guest room 2')
    light = Actuator("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Light Bulp", "Elysian Tech", "Lumina Glow 4000")
    DEMO_HOUSE.register_device(guest_room_2, light)

    bathroom_2 = DEMO_HOUSE.register_room(first_floor, room_size=9.25, room_name='Bathroom 2')
    dehumidifier = Actuator("9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "Dehumidifier", "ArcaneTech Solutions",
                            "Hydra Dry 8000")
    DEMO_HOUSE.register_device(bathroom_2, dehumidifier)

    office = DEMO_HOUSE.register_room(first_floor, room_size=11.75, room_name='Office')
    plug = Actuator("1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "Smart Plug", "MysticEnergy Innovations", "FlowState X")
    DEMO_HOUSE.register_device(office, plug)

    guest_room_3 = DEMO_HOUSE.register_room(first_floor, room_size=10, room_name='Guest room 3')
    air_quality = Sensor("7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "Air Quality Sensor", "CelestialSense Technologies",
                         "AeroGuard Pro")
    DEMO_HOUSE.register_device(guest_room_3, air_quality)

    dressing_room = DEMO_HOUSE.register_room(first_floor, room_size=4, room_name='Dressing room')

    master_bedroom = DEMO_HOUSE.register_room(first_floor, room_size=17, room_name='Master bedroom')
    smart_oven = Actuator("8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "Smart Oven", "AetherCorp", "Pheonix HEAT 333")
    DEMO_HOUSE.register_device(master_bedroom, smart_oven)

    temp_sensor = Sensor("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "Temperature Sensor", "AetherCorp", "SmartTemp 42")
    DEMO_HOUSE.register_device(master_bedroom, temp_sensor)

    print(DEMO_HOUSE)
