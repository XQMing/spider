# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "_lxsdk_cuid=1639b587664c8-04bdb5a9ad9fbd-1571466f-1fa400-1639b587665c8; \
    _lxsdk=1639b587664c8-04bdb5a9ad9fbd-1571466f-1fa400-1639b587665c8; _hc.v=057134b3-bbd7-de67-3c9e-ba04e8bba211.1527319656; \
    dper=2f6a5634387a996d939900142143d70f713bebecfa06265f28a8e5275dba3f359ca6b1207236abc8a30c9325cc81dea945bc3b106f30a02aaaaf0feeb05823488e689ad885349663fabc224ab6c2b313fbe603a0d14c9744ea0a831b2ff7ab1a; \
    ua=mInQ_532; ctu=383b4eeb970a809dd2f534730b186b408f4051ef51185351a1e8ae617f9191df; aburl=1; ll=7fd06e815b796be3df069dec7836c3df; \
    _lx_utm=utm_source%3Dsogou%26utm_medium%3Dorganic; cy=1; cye=shanghai; s_ViewType=10; _lxsdk_s=164c194dc21-6a9-f3d-2eb%7C%7C258"
    trans = transCookie(cookie)
    print(trans.stringToDict())