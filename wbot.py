import pywhatkit as kit
import json

# JSON data (Replace this with your actual data source if loading from a file)
data =[
    {
        "_id": "67a0c1b6a7c8c01ab3314f66",
        "name": "Nithya",
        "contact": "9585028220",
        "eventName": "Illam thedi kalvi",
        "eventDate": "2025-02-03",
        "createdAt": "2025-02-03T13:16:38.433Z",
        "__v": 0
    },
    {
        "_id": "67a0c851a7c8c01ab3314f6c",
        "name": "Parthiban ",
        "contact": "6380121139",
        "eventName": "Book shows",
        "eventDate": "2025-02-03",
        "createdAt": "2025-02-03T13:44:49.832Z",
        "__v": 0
    },
    {
        "_id": "67a0c924a7c8c01ab3314f76",
        "name": "Praveen Kumar ",
        "contact": "7904239495",
        "eventName": "Thappatam ",
        "eventDate": "2025-02-10",
        "createdAt": "2025-02-03T13:48:20.551Z",
        "__v": 0
    },
    {
        "_id": "67a0cc7ba7c8c01ab3314f8c",
        "name": "Manikandan",
        "contact": "9600356418",
        "eventName": "Baby shower",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-03T14:02:35.187Z",
        "__v": 0
    },
    {
        "_id": "67a0ccaba7c8c01ab3314f90",
        "name": "Manikandan",
        "contact": "9600356418",
        "eventName": "Wedding",
        "eventDate": "2025-11-10",
        "createdAt": "2025-02-03T14:03:23.898Z",
        "__v": 0
    },
    {
        "_id": "67a0ccd5a7c8c01ab3314f92",
        "name": "Manikandan",
        "contact": "9600356418",
        "eventName": "Baby shower",
        "eventDate": "2025-12-24",
        "createdAt": "2025-02-03T14:04:05.918Z",
        "__v": 0
    },
    {
        "_id": "67a0ce7ca7c8c01ab3314f9c",
        "name": "Sunil",
        "contact": "949494994",
        "eventName": "",
        "eventDate": "2025-02-21",
        "createdAt": "2025-02-03T14:11:08.668Z",
        "__v": 0
    },
    {
        "_id": "67a0cf8da7c8c01ab3314fa0",
        "name": "B.TARUM",
        "contact": "9790834287",
        "eventName": "WEDDING ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-03T14:15:41.442Z",
        "__v": 0
    },
    {
        "_id": "67a0d1cba7c8c01ab3314fa8",
        "name": "B.TARUM",
        "contact": "9790834287",
        "eventName": "WEDDING ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-03T14:25:15.598Z",
        "__v": 0
    },
    {
        "_id": "67a0d21da7c8c01ab3314faa",
        "name": "B.TARUM",
        "contact": "9790834287",
        "eventName": "WEDDING ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-03T14:26:37.448Z",
        "__v": 0
    },
    {
        "_id": "67a0d2f8a7c8c01ab3314fb2",
        "name": "Rakshith",
        "contact": "9361647205",
        "eventName": "Wedding ",
        "eventDate": "2025-05-05",
        "createdAt": "2025-02-03T14:30:16.487Z",
        "__v": 0
    },
    {
        "_id": "67a0d300a7c8c01ab3314fb6",
        "name": "Nantha Kumar M",
        "contact": "9600035412",
        "eventName": "Birthday",
        "eventDate": "1974-05-30",
        "createdAt": "2025-02-03T14:30:24.429Z",
        "__v": 0
    },
    {
        "_id": "67a0d317a7c8c01ab3314fb8",
        "name": "Rinkesh",
        "contact": "9498008475",
        "eventName": "Birthday",
        "eventDate": "2025-04-04",
        "createdAt": "2025-02-03T14:30:47.644Z",
        "__v": 0
    },
    {
        "_id": "67a0d794a7c8c01ab3314fc6",
        "name": "Marish",
        "contact": "8754996699",
        "eventName": "Birthday ",
        "eventDate": "2025-02-10",
        "createdAt": "2025-02-03T14:49:56.406Z",
        "__v": 0
    },
    {
        "_id": "67a0d8d1a7c8c01ab3314fd1",
        "name": "Vishnu priyanka.R",
        "contact": "9489003834",
        "eventName": "Birthday ",
        "eventDate": "2025-03-04",
        "createdAt": "2025-02-03T14:55:13.742Z",
        "__v": 0
    },
    {
        "_id": "67a0d8eea7c8c01ab3314fd3",
        "name": "Sri",
        "contact": "9790323321",
        "eventName": "Book fair",
        "eventDate": "2025-02-03",
        "createdAt": "2025-02-03T14:55:42.889Z",
        "__v": 0
    },
    {
        "_id": "67a0dceda7c8c01ab3314fe2",
        "name": "yuvaraj",
        "contact": "9364104730",
        "eventName": "Birthday ",
        "eventDate": "2025-04-23",
        "createdAt": "2025-02-03T15:12:45.576Z",
        "__v": 0
    },
    {
        "_id": "67a0df37a7c8c01ab3314fed",
        "name": "Kesavan ",
        "contact": "7871207667",
        "eventName": "Friend birthday ",
        "eventDate": "2025-09-04",
        "createdAt": "2025-02-03T15:22:31.240Z",
        "__v": 0
    },
    {
        "_id": "67a0df73a7c8c01ab3314fef",
        "name": "Sabari T",
        "contact": "7305483904",
        "eventName": "Wedding",
        "eventDate": "2025-05-20",
        "createdAt": "2025-02-03T15:23:31.468Z",
        "__v": 0
    },
    {
        "_id": "67a0e078a7c8c01ab3314ff5",
        "name": "Princy Diana A",
        "contact": "9629481372",
        "eventName": "Wedding",
        "eventDate": "2025-06-21",
        "createdAt": "2025-02-03T15:27:52.638Z",
        "__v": 0
    },
    {
        "_id": "67a0e247a7c8c01ab3314ffc",
        "name": "Balaji subramanian",
        "contact": "9361616136",
        "eventName": "Book fair ",
        "eventDate": "2025-02-03",
        "createdAt": "2025-02-03T15:35:35.151Z",
        "__v": 0
    },
    {
        "_id": "67a102c2a7c8c01ab331500d",
        "name": "Pasupathi ",
        "contact": "9600596461",
        "eventName": "Book fair ",
        "eventDate": "2025-02-03",
        "createdAt": "2025-02-03T17:54:10.460Z",
        "__v": 0
    },
    {
        "_id": "67a105a1a7c8c01ab331500f",
        "name": "Marish",
        "contact": "8754996699",
        "eventName": "Birthday ",
        "eventDate": "2025-02-10",
        "createdAt": "2025-02-03T18:06:25.901Z",
        "__v": 0
    },
    {
        "_id": "67a207c3a7c8c01ab331501d",
        "name": "Sk pandiyan ",
        "contact": "8681857412",
        "eventName": "",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T12:27:47.178Z",
        "__v": 0
    },
    {
        "_id": "67a207dea7c8c01ab331501f",
        "name": "Sk pandiyan ",
        "contact": "8681857412",
        "eventName": "SKP Events ",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T12:28:14.641Z",
        "__v": 0
    },
    {
        "_id": "67a20bd6a7c8c01ab331502d",
        "name": "Kowsalya",
        "contact": "7339276826",
        "eventName": "Kanchipuram book fair",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T12:45:10.399Z",
        "__v": 0
    },
    {
        "_id": "67a20c30a7c8c01ab3315035",
        "name": "D v.Avyukth",
        "contact": "9789590627",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-04T12:46:40.859Z",
        "__v": 0
    },
    {
        "_id": "67a20c68a7c8c01ab3315039",
        "name": "Divya",
        "contact": "6379358522",
        "eventName": "Birthday party ",
        "eventDate": "2025-08-12",
        "createdAt": "2025-02-04T12:47:36.172Z",
        "__v": 0
    },
    {
        "_id": "67a20cf9a7c8c01ab3315042",
        "name": "M.Balaji",
        "contact": "9790443306",
        "eventName": "B.indhumathi",
        "eventDate": "2023-10-27",
        "createdAt": "2025-02-04T12:50:01.387Z",
        "__v": 0
    },
    {
        "_id": "67a20d2ea7c8c01ab3315044",
        "name": "R.kavipriya ",
        "contact": "9597097337",
        "eventName": "Book fair",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T12:50:54.379Z",
        "__v": 0
    },
    {
        "_id": "67a20e68a7c8c01ab3315055",
        "name": "Umapathy  L",
        "contact": "9629419036",
        "eventName": "Birthday wishes ",
        "eventDate": "2025-02-23",
        "createdAt": "2025-02-04T12:56:08.369Z",
        "__v": 0
    },
    {
        "_id": "67a21378a7c8c01ab331508b",
        "name": "Sameera",
        "contact": "7810069357",
        "eventName": "Book fare ",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T13:17:44.840Z",
        "__v": 0
    },
    {
        "_id": "67a2138ca7c8c01ab331508f",
        "name": "Thangapazham",
        "contact": "9566649476",
        "eventName": "Wedding",
        "eventDate": "2025-02-09",
        "createdAt": "2025-02-04T13:18:04.401Z",
        "__v": 0
    },
    {
        "_id": "67a213b4a7c8c01ab3315091",
        "name": "Thangapazham",
        "contact": "9566649476",
        "eventName": "Wedding",
        "eventDate": "2025-02-15",
        "createdAt": "2025-02-04T13:18:44.218Z",
        "__v": 0
    },
    {
        "_id": "67a214b0a7c8c01ab3315099",
        "name": "ThanigaiArasu",
        "contact": "9361390598",
        "eventName": "Wedding ",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T13:22:56.943Z",
        "__v": 0
    },
    {
        "_id": "67a215b0a7c8c01ab33150a8",
        "name": "Dilleeswari ",
        "contact": "9176476396",
        "eventName": "",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T13:27:12.342Z",
        "__v": 0
    },
    {
        "_id": "67a21658a7c8c01ab33150ae",
        "name": "Vicky",
        "contact": "8248182682",
        "eventName": "",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T13:30:00.569Z",
        "__v": 0
    },
    {
        "_id": "67a216dca7c8c01ab33150b4",
        "name": "Divya",
        "contact": "6379358522",
        "eventName": "Birthday party ",
        "eventDate": "2025-08-12",
        "createdAt": "2025-02-04T13:32:12.344Z",
        "__v": 0
    },
    {
        "_id": "67a217b9a7c8c01ab33150bc",
        "name": "Gugan Chakravarthy",
        "contact": "9940659243",
        "eventName": "1st Birthday ",
        "eventDate": "2025-09-26",
        "createdAt": "2025-02-04T13:35:53.016Z",
        "__v": 0
    },
    {
        "_id": "67a21899a7c8c01ab33150cb",
        "name": "Aswin",
        "contact": "9360608759",
        "eventName": "Book fair 2025",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T13:39:37.041Z",
        "__v": 0
    },
    {
        "_id": "67a218aba7c8c01ab33150cd",
        "name": "Tharun",
        "contact": "9894390084",
        "eventName": "Wedding ",
        "eventDate": "2025-02-11",
        "createdAt": "2025-02-04T13:39:55.118Z",
        "__v": 0
    },
    {
        "_id": "67a218aea7c8c01ab33150cf",
        "name": "Tharun",
        "contact": "9894390084",
        "eventName": "Wedding ",
        "eventDate": "2025-02-11",
        "createdAt": "2025-02-04T13:39:58.841Z",
        "__v": 0
    },
    {
        "_id": "67a21902a7c8c01ab33150d3",
        "name": "Ezhilkumaran",
        "contact": "9487574960",
        "eventName": "Wedding",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-04T13:41:22.159Z",
        "__v": 0
    },
    {
        "_id": "67a2194ca7c8c01ab33150d7",
        "name": "B.TARUN",
        "contact": "9790834287",
        "eventName": "WEDDING ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-04T13:42:36.205Z",
        "__v": 0
    },
    {
        "_id": "67a21acba7c8c01ab33150ee",
        "name": "Yuvaraj ",
        "contact": "8883415681",
        "eventName": "Wedding",
        "eventDate": "2025-08-15",
        "createdAt": "2025-02-04T13:48:59.591Z",
        "__v": 0
    },
    {
        "_id": "67a21b3ba7c8c01ab33150f9",
        "name": "Iniyan I",
        "contact": "8637421292",
        "eventName": "Birthday",
        "eventDate": "2025-06-06",
        "createdAt": "2025-02-04T13:50:51.255Z",
        "__v": 0
    },
    {
        "_id": "67a21b95a7c8c01ab33150ff",
        "name": "Thanvik Mithran",
        "contact": "9092027134",
        "eventName": "Baby 1st birthday ",
        "eventDate": "2025-04-24",
        "createdAt": "2025-02-04T13:52:21.418Z",
        "__v": 0
    },
    {
        "_id": "67a21d54a7c8c01ab3315117",
        "name": "Praveen ",
        "contact": "8667475039",
        "eventName": "Wedding ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-04T13:59:48.587Z",
        "__v": 0
    },
    {
        "_id": "67a21e5ca7c8c01ab3315133",
        "name": " B.Prithish",
        "contact": "8344630177",
        "eventName": "My birthday",
        "eventDate": "2025-12-24",
        "createdAt": "2025-02-04T14:04:12.853Z",
        "__v": 0
    },
    {
        "_id": "67a21ea4a7c8c01ab331513e",
        "name": "Anbarasu",
        "contact": "9786647427",
        "eventName": "Wedding anniversary ",
        "eventDate": "2025-05-27",
        "createdAt": "2025-02-04T14:05:24.689Z",
        "__v": 0
    },
    {
        "_id": "67a21eb0a7c8c01ab3315142",
        "name": " B.Prithish",
        "contact": "8344630177",
        "eventName": "My birthday",
        "eventDate": "2025-12-24",
        "createdAt": "2025-02-04T14:05:36.181Z",
        "__v": 0
    },
    {
        "_id": "67a2208ca7c8c01ab3315155",
        "name": "Haripriya  B",
        "contact": "8098770307",
        "eventName": "Baby shower ",
        "eventDate": "2025-04-30",
        "createdAt": "2025-02-04T14:13:32.527Z",
        "__v": 0
    },
    {
        "_id": "67a2245ca7c8c01ab331517c",
        "name": "Umesh Kumar Rajendran",
        "contact": "7904436288",
        "eventName": "Wedding",
        "eventDate": "2025-04-14",
        "createdAt": "2025-02-04T14:29:48.420Z",
        "__v": 0
    },
    {
        "_id": "67a22550a7c8c01ab3315186",
        "name": "Thillai",
        "contact": "6369297919",
        "eventName": "Birthday ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T14:33:52.525Z",
        "__v": 0
    },
    {
        "_id": "67a22594a7c8c01ab331518a",
        "name": "Sanjay raj",
        "contact": "9344338578",
        "eventName": "Birth day ",
        "eventDate": "2025-02-24",
        "createdAt": "2025-02-04T14:35:00.483Z",
        "__v": 0
    },
    {
        "_id": "67a226dda7c8c01ab3315198",
        "name": "Ambedkar",
        "contact": "9655581198",
        "eventName": "Wedding ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T14:40:29.035Z",
        "__v": 0
    },
    {
        "_id": "67a226fca7c8c01ab331519a",
        "name": "Ambedkar",
        "contact": "9655581198",
        "eventName": "Wedding ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T14:41:00.100Z",
        "__v": 0
    },
    {
        "_id": "67a2272ca7c8c01ab331519c",
        "name": "Ambedkar",
        "contact": "9655581198",
        "eventName": "Wedding ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T14:41:48.920Z",
        "__v": 0
    },
    {
        "_id": "67a22761a7c8c01ab33151a2",
        "name": "Ambedkar",
        "contact": "9655581198",
        "eventName": "Wedding ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-04T14:42:41.545Z",
        "__v": 0
    },
    {
        "_id": "67a22b13a7c8c01ab33151cd",
        "name": "Sara",
        "contact": "6381503978",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-04T14:58:27.442Z",
        "__v": 0
    },
    {
        "_id": "67a22ce8a7c8c01ab33151de",
        "name": "Rabitheen ",
        "contact": "9786155024",
        "eventName": "Book fair ",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T15:06:16.949Z",
        "__v": 0
    },
    {
        "_id": "67a22d7ea7c8c01ab33151ec",
        "name": "Sulthana",
        "contact": "9087686436",
        "eventName": "Wedding",
        "eventDate": "2025-07-25",
        "createdAt": "2025-02-04T15:08:46.763Z",
        "__v": 0
    },
    {
        "_id": "67a22e37a7c8c01ab33151fb",
        "name": "K s GOPI ",
        "contact": "8667014626",
        "eventName": "Book fare",
        "eventDate": "2025-02-04",
        "createdAt": "2025-02-04T15:11:51.838Z",
        "__v": 0
    },
    {
        "_id": "67a22e8ea7c8c01ab33151fe",
        "name": "Logesh",
        "contact": "9566273883",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-04T15:13:18.750Z",
        "__v": 0
    },
    {
        "_id": "67a23246a7c8c01ab3315218",
        "name": "Abirami & Mithra",
        "contact": "7305772229",
        "eventName": "Lover's Day",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-04T15:29:10.202Z",
        "__v": 0
    },
    {
        "_id": "67a2335ea7c8c01ab3315228",
        "name": "LAVANYA PRIYA G",
        "contact": "8883714106",
        "eventName": "Birthday",
        "eventDate": "2025-02-23",
        "createdAt": "2025-02-04T15:33:50.506Z",
        "__v": 0
    },
    {
        "_id": "67a23658a7c8c01ab331522c",
        "name": "JaiA",
        "contact": "8220385151",
        "eventName": "Baby shower ",
        "eventDate": "2025-08-02",
        "createdAt": "2025-02-04T15:46:32.428Z",
        "__v": 0
    },
    {
        "_id": "67a23c01a7c8c01ab3315235",
        "name": "Thamizhinba C",
        "contact": "9901611342",
        "eventName": "Birthday ",
        "eventDate": "2025-08-07",
        "createdAt": "2025-02-04T16:10:41.923Z",
        "__v": 0
    },
    {
        "_id": "67a23c42a7c8c01ab3315237",
        "name": "Thamizhinba C",
        "contact": "9901611342",
        "eventName": "Birthday ",
        "eventDate": "2025-08-07",
        "createdAt": "2025-02-04T16:11:46.234Z",
        "__v": 0
    },
    {
        "_id": "67a23c74a7c8c01ab3315239",
        "name": "Thamizhinba C",
        "contact": "9901611342",
        "eventName": "Birthday ",
        "eventDate": "2025-08-07",
        "createdAt": "2025-02-04T16:12:36.855Z",
        "__v": 0
    },
    {
        "_id": "67a2407fa7c8c01ab331523b",
        "name": "Yash",
        "contact": "9940223500",
        "eventName": "Wedding ",
        "eventDate": "2015-02-05",
        "createdAt": "2025-02-04T16:29:51.929Z",
        "__v": 0
    },
    {
        "_id": "67a24360a7c8c01ab331523f",
        "name": "Danushya",
        "contact": "7899015908",
        "eventName": "7th year birthday ",
        "eventDate": "2025-02-27",
        "createdAt": "2025-02-04T16:42:08.478Z",
        "__v": 0
    },
    {
        "_id": "67a249cba7c8c01ab3315244",
        "name": "Saranya",
        "contact": "7904665859",
        "eventName": "7th month baby shower",
        "eventDate": "2025-03-09",
        "createdAt": "2025-02-04T17:09:31.133Z",
        "__v": 0
    },
    {
        "_id": "67a25626a7c8c01ab331524e",
        "name": "THAMIZMANI S & PRABHAVATHI V & ABINAVKRISHNA T",
        "contact": "9840777325",
        "eventName": "Wedding ",
        "eventDate": "2025-09-17",
        "createdAt": "2025-02-04T18:02:14.181Z",
        "__v": 0
    },
    {
        "_id": "67a339dea7c8c01ab3315258",
        "name": "Marish",
        "contact": "8754996699",
        "eventName": "Birthday ",
        "eventDate": "2025-02-10",
        "createdAt": "2025-02-05T10:13:50.147Z",
        "__v": 0
    },
    {
        "_id": "67a357e0a7c8c01ab3315270",
        "name": "Rajashri",
        "contact": "8807454458",
        "eventName": " Book festival ",
        "eventDate": "2025-02-05",
        "createdAt": "2025-02-05T12:21:52.460Z",
        "__v": 0
    },
    {
        "_id": "67a3618ca7c8c01ab331529a",
        "name": "Yokesh ",
        "contact": "9597485756",
        "eventName": "Sunil ",
        "eventDate": "2025-02-05",
        "createdAt": "2025-02-05T13:03:08.618Z",
        "__v": 0
    },
    {
        "_id": "67a36518a7c8c01ab33152aa",
        "name": "Sabari",
        "contact": "8838242855",
        "eventName": "Birthday ",
        "eventDate": "2025-03-31",
        "createdAt": "2025-02-05T13:18:16.024Z",
        "__v": 0
    },
    {
        "_id": "67a365f7a7c8c01ab33152b4",
        "name": "Sankar ",
        "contact": "9751833",
        "eventName": "Navi tharum nayam nool",
        "eventDate": "2025-02-05",
        "createdAt": "2025-02-05T13:21:59.730Z",
        "__v": 0
    },
    {
        "_id": "67a37466a7c8c01ab3315334",
        "name": "Suganya",
        "contact": "7667288810",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-05T14:23:34.163Z",
        "__v": 0
    },
    {
        "_id": "67a377ffa7c8c01ab331534b",
        "name": "Jerry",
        "contact": "07603883143",
        "eventName": "Birthday ",
        "eventDate": "2025-12-12",
        "createdAt": "2025-02-05T14:38:55.787Z",
        "__v": 0
    },
    {
        "_id": "67a381aaa7c8c01ab3315382",
        "name": "Vijay vaishu",
        "contact": "9344937324",
        "eventName": "Lovers day",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-05T15:20:10.993Z",
        "__v": 0
    },
    {
        "_id": "67a385caa7c8c01ab33153ad",
        "name": "Murali",
        "contact": "9944098109",
        "eventName": "",
        "eventDate": "2025-02-05",
        "createdAt": "2025-02-05T15:37:46.226Z",
        "__v": 0
    },
    {
        "_id": "67a385cca7c8c01ab33153af",
        "name": "Yoga priya",
        "contact": "8248082585",
        "eventName": "Wedding ",
        "eventDate": "2025-04-30",
        "createdAt": "2025-02-05T15:37:48.316Z",
        "__v": 0
    },
    {
        "_id": "67a38656a7c8c01ab33153ba",
        "name": "Duraipandiyan ",
        "contact": "8124504282",
        "eventName": "Marriage ",
        "eventDate": "2025-07-07",
        "createdAt": "2025-02-05T15:40:06.556Z",
        "__v": 0
    },
    {
        "_id": "67a3865da7c8c01ab33153bc",
        "name": "Yoga priya",
        "contact": "8248082585",
        "eventName": "Wedding ",
        "eventDate": "2025-07-07",
        "createdAt": "2025-02-05T15:40:13.910Z",
        "__v": 0
    },
    {
        "_id": "67a3876ca7c8c01ab33153c4",
        "name": "Jeevarekha Ganapathy ",
        "contact": "9585225536",
        "eventName": "Wedding  anniversary ",
        "eventDate": "2025-06-17",
        "createdAt": "2025-02-05T15:44:44.789Z",
        "__v": 0
    },
    {
        "_id": "67a3877ea7c8c01ab33153c6",
        "name": "Jeevarekha Ganapathy ",
        "contact": "9585225536",
        "eventName": "Wedding  anniversary ",
        "eventDate": "2025-06-17",
        "createdAt": "2025-02-05T15:45:02.191Z",
        "__v": 0
    },
    {
        "_id": "67a47978a7c8c01ab33153e2",
        "name": "James",
        "contact": "9894814979",
        "eventName": "Magic",
        "eventDate": "2025-02-07",
        "createdAt": "2025-02-06T08:57:28.496Z",
        "__v": 0
    },
    {
        "_id": "67a4ad8ea7c8c01ab331540d",
        "name": "Vijay ",
        "contact": "8667382826",
        "eventName": "House warming ",
        "eventDate": "2025-02-11",
        "createdAt": "2025-02-06T12:39:42.109Z",
        "__v": 0
    },
    {
        "_id": "67a4b0b2a7c8c01ab3315419",
        "name": "Murali",
        "contact": "8825830689",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-06T12:53:06.454Z",
        "__v": 0
    },
    {
        "_id": "67a4b4bba7c8c01ab331542c",
        "name": "Devadharshan",
        "contact": "9787123895",
        "eventName": "Wedding ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:10:19.101Z",
        "__v": 0
    },
    {
        "_id": "67a4b53fa7c8c01ab3315430",
        "name": "Iniya sri ",
        "contact": "9080543885",
        "eventName": "Wedding video ",
        "eventDate": "2025-05-18",
        "createdAt": "2025-02-06T13:12:31.838Z",
        "__v": 0
    },
    {
        "_id": "67a4b9bca7c8c01ab3315459",
        "name": "Swethaa kj",
        "contact": "9500360277",
        "eventName": "Birthday ",
        "eventDate": "2000-04-28",
        "createdAt": "2025-02-06T13:31:40.932Z",
        "__v": 0
    },
    {
        "_id": "67a4ba01a7c8c01ab331545d",
        "name": "Bhuvanesh",
        "contact": "9566366941",
        "eventName": "Book festival",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:32:49.853Z",
        "__v": 0
    },
    {
        "_id": "67a4ba64a7c8c01ab3315467",
        "name": "Murugan",
        "contact": "6374181853",
        "eventName": "Book festival",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:34:28.997Z",
        "__v": 0
    },
    {
        "_id": "67a4ba78a7c8c01ab331546c",
        "name": "Seenu",
        "contact": "6382986906",
        "eventName": "Book festival",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:34:48.132Z",
        "__v": 0
    },
    {
        "_id": "67a4ba88a7c8c01ab331546f",
        "name": "Seenu",
        "contact": "6382986906",
        "eventName": "Book festival",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:35:04.937Z",
        "__v": 0
    },
    {
        "_id": "67a4bad4a7c8c01ab3315473",
        "name": "AKSHAYA.M",
        "contact": "9942413139",
        "eventName": "Birthday ",
        "eventDate": "2025-04-21",
        "createdAt": "2025-02-06T13:36:20.050Z",
        "__v": 0
    },
    {
        "_id": "67a4bd20a7c8c01ab3315495",
        "name": "THAMIZHARASU KUMARAN",
        "contact": "9600987325",
        "eventName": "Book Fair",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T13:46:08.189Z",
        "__v": 0
    },
    {
        "_id": "67a4beb9a7c8c01ab331549b",
        "name": "S.Elakiya",
        "contact": "7845833969",
        "eventName": "Birthday ",
        "eventDate": "2025-02-26",
        "createdAt": "2025-02-06T13:52:57.407Z",
        "__v": 0
    },
    {
        "_id": "67a4bf30a7c8c01ab331549f",
        "name": "Janarthanan",
        "contact": "8190997384",
        "eventName": "Wedding anniversary ",
        "eventDate": "2025-02-14",
        "createdAt": "2025-02-06T13:54:56.561Z",
        "__v": 0
    },
    {
        "_id": "67a4c0b3a7c8c01ab33154b9",
        "name": "S. Deva",
        "contact": "9043585315",
        "eventName": "Book fair",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T14:01:23.734Z",
        "__v": 0
    },
    {
        "_id": "67a4c441a7c8c01ab33154ec",
        "name": "Boopathiraja R",
        "contact": "9677576246",
        "eventName": "Wedding ",
        "eventDate": "2016-09-05",
        "createdAt": "2025-02-06T14:16:33.407Z",
        "__v": 0
    },
    {
        "_id": "67a4c701a7c8c01ab3315506",
        "name": "Surya",
        "contact": "8148644655",
        "eventName": "Nothing ",
        "eventDate": "2025-02-08",
        "createdAt": "2025-02-06T14:28:17.369Z",
        "__v": 0
    },
    {
        "_id": "67a4c730a7c8c01ab3315508",
        "name": "Surya",
        "contact": "8148644655",
        "eventName": "Marage",
        "eventDate": "2025-02-08",
        "createdAt": "2025-02-06T14:29:04.838Z",
        "__v": 0
    },
    {
        "_id": "67a4c7ffa7c8c01ab3315511",
        "name": "Tharun sri",
        "contact": "9894390084",
        "eventName": "Wedding ",
        "eventDate": "2025-02-13",
        "createdAt": "2025-02-06T14:32:31.481Z",
        "__v": 0
    },
    {
        "_id": "67a4c893a7c8c01ab3315515",
        "name": "Dhanalakshmi ",
        "contact": "8608005452",
        "eventName": "Birthday ",
        "eventDate": "2025-03-29",
        "createdAt": "2025-02-06T14:34:59.060Z",
        "__v": 0
    },
    {
        "_id": "67a4ca4ea7c8c01ab3315534",
        "name": "Madhavan",
        "contact": "8754606249",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-06T14:42:22.060Z",
        "__v": 0
    },
    {
        "_id": "67a4ca4ea7c8c01ab3315536",
        "name": "Madhavan",
        "contact": "8754606249",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-06T14:42:22.819Z",
        "__v": 0
    },
    {
        "_id": "67a4cae8a7c8c01ab331553d",
        "name": "Vithaga Venthan ",
        "contact": "9787474777",
        "eventName": "Wedding ",
        "eventDate": "2025-02-01",
        "createdAt": "2025-02-06T14:44:56.020Z",
        "__v": 0
    },
    {
        "_id": "67a4cbf4a7c8c01ab3315547",
        "name": "Rajini",
        "contact": "6380069711",
        "eventName": "",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T14:49:24.502Z",
        "__v": 0
    },
    {
        "_id": "67a4cd49a7c8c01ab3315553",
        "name": "Jayasumathy ",
        "contact": "9629254537",
        "eventName": "Birthday ",
        "eventDate": "2025-02-20",
        "createdAt": "2025-02-06T14:55:05.484Z",
        "__v": 0
    },
    {
        "_id": "67a4cef6a7c8c01ab331556a",
        "name": "Dhamayanthi ",
        "contact": "9791613476",
        "eventName": "Birthday ",
        "eventDate": "2025-06-05",
        "createdAt": "2025-02-06T15:02:14.293Z",
        "__v": 0
    },
    {
        "_id": "67a4cf14a7c8c01ab331556e",
        "name": "Thanigaiarasu ",
        "contact": "9791613476",
        "eventName": "Birthday ",
        "eventDate": "2025-03-30",
        "createdAt": "2025-02-06T15:02:44.105Z",
        "__v": 0
    },
    {
        "_id": "67a4cf4aa7c8c01ab3315574",
        "name": "Thiruvengidam ",
        "contact": "09445162732",
        "eventName": "Wedding ",
        "eventDate": "2025-05-27",
        "createdAt": "2025-02-06T15:03:38.678Z",
        "__v": 0
    },
    {
        "_id": "67a4cf51a7c8c01ab3315576",
        "name": "Santhosh ",
        "contact": "9994502235",
        "eventName": "Ur invite ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T15:03:45.904Z",
        "__v": 0
    },
    {
        "_id": "67a4cfa2a7c8c01ab3315578",
        "name": "Santhosh ",
        "contact": "9994502235",
        "eventName": "Ur invite ",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T15:05:06.010Z",
        "__v": 0
    },
    {
        "_id": "67a4d0e3a7c8c01ab3315584",
        "name": "Roshan",
        "contact": "9345277498",
        "eventName": "Birthday ",
        "eventDate": "2025-11-28",
        "createdAt": "2025-02-06T15:10:27.428Z",
        "__v": 0
    },
    {
        "_id": "67a4d136a7c8c01ab331558a",
        "name": "Rohan",
        "contact": "95666354847",
        "eventName": "Birthday",
        "eventDate": "2025-09-10",
        "createdAt": "2025-02-06T15:11:50.939Z",
        "__v": 0
    },
    {
        "_id": "67a4d16ba7c8c01ab331558e",
        "name": "saravanan ",
        "contact": "8825973499",
        "eventName": "Ourinites",
        "eventDate": "2025-02-06",
        "createdAt": "2025-02-06T15:12:43.422Z",
        "__v": 0
    },
    {
        "_id": "67a4d1cfa7c8c01ab3315594",
        "name": "Arpittamrta A",
        "contact": "6382116676",
        "eventName": "Birthday",
        "eventDate": "2025-03-23",
        "createdAt": "2025-02-06T15:14:23.310Z",
        "__v": 0
    },
    {
        "_id": "67a5a3bbd5b28e96da71ef4e",
        "name": "Lekha shree",
        "contact": "8248828108",
        "eventName": "",
        "eventDate": "",
        "createdAt": "2025-02-07T06:10:03.767Z",
        "__v": 0
    },
    {
        "_id": "67a5b63fd5b28e96da71ef50",
        "name": "Jeevarekha Ganapathy ",
        "contact": "9585225536",
        "eventName": "Wedding  anniversary ",
        "eventDate": "2025-06-17",
        "createdAt": "2025-02-07T07:29:03.907Z",
        "__v": 0
    }
]

# Extract numbers and format them correctly (assuming India country code +91)
numbers = [f"+91{entry['contact']}" for entry in data]

# Message to send
message = """Greetings From OurInvites 🌟

Received Your Free Invitation Request, happy to assist You!

Please Share Your Event details to Draft an Invitation!
"""

# Sending messages one by one
for num in numbers:
    try:
        print(f"Sending message to {num}...")
        kit.sendwhatmsg_instantly(num, message, wait_time=10, tab_close=True)
    except Exception as e:
        print(f"Failed to send message to {num}: {e}")

print("All messages attempted!")
