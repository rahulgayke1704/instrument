"""
2️⃣ Guitar, Drum, Flute class तयार कर:
- प्रत्येक class Instrument inherit करेल
- play_sound() method override कर
3️⃣ एक polymorphic function तयार कर:
- नाव: perform(instrument_obj)
- त्यात instrument_obj.play_sound() call कर
4️⃣ Test कर:
- प्रत्येक instrument चा object तयार कर
- perform() function वापरून sound play कर

"""


class Instrument :
    def play_sound(self):
        print("method generic sound")

