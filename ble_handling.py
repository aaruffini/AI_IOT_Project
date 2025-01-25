import asyncio
from bleak import BleakClient, BleakScanner



async def main():
    ble_address = ""
    characteristic_uuid = ""
    async with BleakClient(ble_address) as client:
        data = await client.read_gatt_char(characteristic_uuid)
        data[0] = 1
        await client.write_gatt_char(characteristic_uuid, data)


asyncio.run(main())