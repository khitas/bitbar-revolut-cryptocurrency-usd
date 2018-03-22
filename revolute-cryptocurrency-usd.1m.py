#!/usr/bin/python
# coding=utf-8

# <bitbar.title>Revolut Cryptocurrency Rates</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Chytas Constantinos </bitbar.author>
# <bitbar.author.github>khitas</bitbar.author.github>
# <bitbar.desc>Displays Revolut prices of Bitcoin, Ethereum, Litecoin.</bitbar.desc>
# <bitbar.image></bitbar.image>
# <bitbar.dependencies>bash, python</bitbar.dependencies>
#
# I hope this plugin provides value for you and if you feel like it, tips are always appreciated.
# Bitcoin: 1CthBGP5nqZYUN1u5LLtqPBVxPVNfwW8vU
# Litecoin: LTy2yjddpoFwDkgHZUrBzFwqfQadJ7ZBcW

import json
from urllib import urlopen

btc_data = urlopen('https://www.revolut.com/api/quote/internal?symbol=BTCUSD').read()
btc_coin = json.loads(btc_data)

eth_data = urlopen('https://www.revolut.com/api/quote/internal?symbol=ETHUSD').read()
eth_coin = json.loads(eth_data)

ltc_data = urlopen('https://www.revolut.com/api/quote/internal?symbol=LTCUSD').read()
ltc_coin = json.loads(ltc_data)

####### Revolut ########

#Btc Price
btc_price = float(btc_coin[0]['rate'])
print (' {:,.2f} | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA4UlEQVQ4jZ3TL0tDYRQH4KdZLAaTmBWzNotZP4HoilVkH0EM1hks2gS/wGBFZBaLwSBY558qE2GyOLmWI74b997d3QOnHH7ngQPvS349oo0VjLBbkCusJ3Swigx7VZaaOIvu4xVXAbRxgMUy4CHCZT3EdhmygM8Id7GENRwnyPO0U3oR7EzMX2L+MSswh338xPyyKjDCIFnM8I2dqkAPp2jhbgJqzHLCXzUS4LYOsJkA3bzFZWzhK0L32IhZE+8JcJIHXJj+kDLcYD4POMR5dB9vuPb/lI+wXnz5eNX6TLWAX4elYGpsY4K9AAAAAElFTkSuQmCC color=#000000'.format(btc_price))

#Eth Price
eth_price = float(eth_coin[0]['rate'])
print (' {:,.2f} |  image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABWUlEQVQ4jZWSMUsDQRCF18rGpLgQktzOvJmdKyw0gthpGbAylRaCoOI/8FcIIjE/wSKtlWWEpNIqjY1YWShoI1rYGYxFTAjiHcnrFuZ9O+8xzmUIHlshRj1rJlVRFOWN5N6ANsrlpZkBytIwxkdg7gbm7kxmLvFyAL5GgER0IER70/9O0klEB5MAY3mJoig/xeq8m4gOEtFBAJ4MuBq9DWhmmouuuKCQZ2N+MODcCK0AnCpzQ0luDdInopVUQADqwcuZQnr/RHg0oKnMx6kAYT4KkM/xyhOAYQTpG+EkHRDH6yGOFw3S+gtQko7Esgrva6kAn8sVFNILHvuI4w2DXAfmi+CxA+9rCulRiaqZRQbmTYN8K8lNAqxVKhUxksvhRhn5J2VA87e49/FNAG3n3NxUAOfcvAF3ow4M8kaFgp/W7JxzjkpUNcarknSEaHsm80jKfKjAQdbMD2ZLarpdKrocAAAAAElFTkSuQmCC color=#000000'.format(eth_price))

#Ltc Price
ltc_price = float(ltc_coin[0]['rate'])
print (' {:,.2f} |  image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAz0lEQVQ4jZXSsUoDQRCA4U+wTGfAQtJZWQXzAGnTpDeFZUR7bX0UH0BJnUcIIa1VGklnI9gFRDmLu8BkueP2BoZdlv3/YXaW+hihCDltuNcYD4ngvKvgJcC7rjC8B8FbOB/hrg3u4S8InnCKZ/xg1iYYO+5/jnW1/8RFm+AxEfxW6wL9NhheE8E3bnPAQ3wEeINBLthXvnisft+l8i6BC1znwgPliLYB3ivHlxVXGGIZBKtK0JQndaKvmjaacpLClx3gAmep4Eb5aXJye4D+ASQXXKJgt99qAAAAAElFTkSuQmCC color=#000000'.format(ltc_price))


