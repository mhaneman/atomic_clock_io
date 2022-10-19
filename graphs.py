import matplotlib.pyplot as plt
import numpy as np
import asyncio

"""
potential implementation of an async matplotlib graph

"""

async def get_new_data():
    await asyncio.sleep(10)
    return np.random.randint(10)

async def live_graph():
    x_data = [0]
    y_data = [0]

    plt.ion()
    fig = plt.figure()
    while True:
        y_data.append(await get_new_data())
        x_data.append(x_data[-1] + 1)
        plt.scatter(x=x_data, y=y_data)
        fig.canvas.draw()
        fig.canvas.flush_events()


if __name__ == "__main__":
    asyncio.run(live_graph())