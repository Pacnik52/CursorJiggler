# MouseJiggler

It Jiggles the cursor from time to time

## Building exe file

pyinstaller --onefile --noconsole --add-data "jigglerIcon.png;." --name "CursorJiggler" --icon=jigglerIcon.ico jiggler.py