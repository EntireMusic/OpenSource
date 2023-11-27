import json
import aiohttp
import asyncio


async def proxy_checker(input_proxies):
    async def check_proxy(prox, session):
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
        }
        try:
            async with session.get('https://konstrada.gov.ua/', proxy=f'http://{prox}', headers=head, timeout=10) as r:
                if r.status == 200:
                    print(f'VALID {prox}')
                    return prox
        except Exception as e:
            print(f'Invalid proxy {prox}, {type(e)}')

    async with aiohttp.ClientSession() as aio_session:
        tasks = [check_proxy(p, aio_session) for p in input_proxies]
        results = await asyncio.gather(*tasks)
        return [i for i in results if i is not None]


async def main():
    with (open('input_proxies.json', 'r', encoding='utf8') as in_proxy,
          open('valid_proxies.json', 'w', encoding='utf8') as out_proxy):
        proxies = json.load(in_proxy)
        json.dump(await proxy_checker(proxies), out_proxy, indent='\n')


if __name__ == "__main__":
    asyncio.run(main())
