from twint.run import Twint, Search
from twint.config import Config

c = Config()
c.Username = "realDonaldTrump"
c.Search = "great"

Search(c)
