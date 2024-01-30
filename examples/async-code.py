import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return (await response.json())["title"]


async def fetch_all(urls):
    return await asyncio.gather(*map(fetch_data, urls))


if __name__ == "__main__":
    print(asyncio.run(fetch_all([
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ])))
