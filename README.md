# oxford_dictionary

> INSTALLATION:
```
pip install git+https://github.com/ShindouAris/oxford_dictionary.git
```

> Usage (Not async):
```python
from oxford_dictionary import OxfordDictionary

def check_word(word: str) -> bool:
    dictionary = OxfordDictionary()
    check_input = dictionary.check_word(word)
    return check_input

if __name__ == '__main__':
    while True:
        user_input = input("> ")
        print(check_word(user_input))
```

> Usage (with async):

```python
from oxford_dictionary import OxfordDictionary
from asyncio import run

async def check_word(word: str) -> bool:
    dictionary = OxfordDictionary()
    check_input = await dictionary.check_word_async(word)
    return check_input

if __name__ == '__main__':
    while True:
        user_input = input("> ")
        print(run(check_word(user_input)))
```