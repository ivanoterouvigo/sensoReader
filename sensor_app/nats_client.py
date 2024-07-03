import asyncio
from nats.aio.client import Client as NATS

class NATSClient:
    def __init__(self):
        self.nc = NATS()

    async def connect(self):
        await self.nc.connect("nats://localhost:4222")

    async def publish(self, subject, msg):
        await self.nc.publish(subject, msg)

    async def close(self):
        await self.nc.close()