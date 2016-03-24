# DTDI Geologic Time Resolver service

This service returns a list (in JSON) of geologic time intervals that intersect with or are encompassed by the specified min and max age (specified in Millions of years ago).

example:

locally running instance:
``curl "127.0.0.1:5000/resolve-intersects?min=1000&max=1200"``

public service:
``curl "https://deeptime.tw.rpi.edu/geologic-intervals/resolve-intersects?min=1000&max=1200"``

results:

```
[  
   {  
      "pid":0,
      "lag":541,
      "typ":"int",
      "col":"#F73563",
      "eag":2500,
      "nam":"Proterozoic",
      "rid":[  
         47900
      ],
      "lvl":1,
      "oid":752
   },
   {  
      "pid":752,
      "lag":541,
      "typ":"int",
      "col":"#FEB342",
      "eag":1000,
      "nam":"Neoproterozoic",
      "rid":[  
         47900
      ],
      "lvl":2,
      "oid":754
   },
   {  
      "pid":752,
      "lag":1000,
      "typ":"int",
      "col":"#FDB462",
      "eag":1600,
      "nam":"Mesoproterozoic",
      "rid":[  
         47900
      ],
      "lvl":2,
      "oid":755
   },
   {  
      "pid":754,
      "lag":850,
      "typ":"int",
      "col":"#FEBF4E",
      "eag":1000,
      "nam":"Tonian",
      "rid":[  
         47900
      ],
      "lvl":3,
      "oid":763
   },
   {  
      "pid":755,
      "lag":1000,
      "typ":"int",
      "col":"#FED99A",
      "eag":1200,
      "nam":"Stenian",
      "rid":[  
         47900
      ],
      "lvl":3,
      "oid":764
   },
   {  
      "pid":755,
      "lag":1200,
      "typ":"int",
      "col":"#F3CC8A",
      "eag":1400,
      "nam":"Ectasian",
      "rid":[  
         47900
      ],
      "lvl":3,
      "oid":765
   }
]
```