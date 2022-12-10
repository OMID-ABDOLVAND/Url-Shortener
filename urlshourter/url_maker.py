import random
import string


def make_short_url():
    charecter = string.ascii_lowercase
    url = ''.join(random.sample(charecter, 10))
    return url
