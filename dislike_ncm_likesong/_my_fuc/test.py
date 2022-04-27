import requests

cookies = {
    'MUSIC_U': 'fb2c06d4fb32ba6915ae98c23d1510ade5b24f692b45f1ffd2b39d7f543e79c7a3a781453231e5e5f1400cbdda37fa846852337e8e2c4bf1404df88cdb2565ceacba965e9c2dc96318469ca8a0280ebd43c37b5d7deb5370d215f21693bd59e3d03722fa6a4c4232',
    '__csrf': '9ed41fe1e219261794cfa3df508abe39',
    'NMTID': '00OkPhFckglDLRbYU6msOBqoFPEGB0AAAGAT3gTEg',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'MUSIC_U=fb2c06d4fb32ba6915ae98c23d1510ade5b24f692b45f1ffd2b39d7f543e79c7a3a781453231e5e5f1400cbdda37fa846852337e8e2c4bf1404df88cdb2565ceacba965e9c2dc96318469ca8a0280ebd43c37b5d7deb5370d215f21693bd59e3d03722fa6a4c4232; __csrf=9ed41fe1e219261794cfa3df508abe39; NMTID=00OkPhFckglDLRbYU6msOBqoFPEGB0AAAGAT3gTEg',
}

params = {
    'id': '34731033',
    'like': 'false',
}

response = requests.get('http://localhost:3000/like', headers=headers, params=params, cookies=cookies)
print(response.text)
