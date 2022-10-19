import numpy as np

def hardware_init():
    pass

async def get_data():
    await asyncio.sleep(1)
    return np.random.randint(1, 100, 1000)
    

