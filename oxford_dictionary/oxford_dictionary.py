from aiohttp import ClientSession
from fake_useragent import UserAgent
from requests import get


class OxfordDictionary:
    def __init__(self):
        pass

    @staticmethod
    def gen_user_agents() -> str:
        return f"{UserAgent.chrome}"

    async def check_word_async(self, word):
        headers = {"User-Agent": self.gen_user_agents()}
        async with ClientSession() as session:
            response = await session.get(f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}", headers=headers)

            if response.ok:
                return True
            elif response.status == 404:
                return False
            else:
                return response.status

    def check_word(self, word):

        headers = {"User-Agent": self.gen_user_agents()}

        resp = get(f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}", headers=headers)

        if resp.ok:
            return True
        elif resp.status_code == 404:
            return False
        else:
            return resp.status_code
