"""
Scalable URL Shortener Implementation using Base62 encoding.
"""

import string
from typing import Optional

BASE62 = string.digits + string.ascii_letters  # 0-9, a-z, A-Z (length 62)


def encode_base62(num: int) -> str:
    """Encode an integer ID into a Base62 string."""
    if num == 0:
        return BASE62[0]
    chars = []
    base = len(BASE62)
    while num > 0:
        chars.append(BASE62[num % base])
        num //= base
    return "".join(reversed(chars))


def decode_base62(code: str) -> int:
    """Decode a Base62 string back into an integer ID."""
    num = 0
    base = len(BASE62)
    for char in code:
        num = num * base + BASE62.index(char)
    return num


class URLShortenerService:
    def __init__(self, base_url: str = "https://tiny.url/"):
        self.base_url = base_url
        self.counter = 1000000000  # Start with 1B for 6-7 char length
        self.id_to_url = {}
        self.url_to_code = {}

    def shorten(self, long_url: str) -> str:
        if long_url in self.url_to_code:
            return self.base_url + self.url_to_code[long_url]

        current_id = self.counter
        self.counter += 1

        code = encode_base62(current_id)
        self.id_to_url[code] = long_url
        self.url_to_code[long_url] = code
        return self.base_url + code

    def resolve(self, short_code: str) -> Optional[str]:
        # Strip domain if full URL passed
        if short_code.startswith(self.base_url):
            short_code = short_code[len(self.base_url):]
        return self.id_to_url.get(short_code)


if __name__ == "__main__":
    service = URLShortenerService()
    test_url = "https://example.com/system-design/distributed-architecture-guide?query=true"
    shortened = service.shorten(test_url)
    print(f"Original URL: {test_url}")
    print(f"Shortened URL: {shortened}")

    resolved = service.resolve(shortened)
    print(f"Resolved URL:  {resolved}")
    assert test_url == resolved
    print("Verification Passed successfully!")
