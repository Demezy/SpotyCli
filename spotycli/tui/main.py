import pytermgui as ptg

with ptg.WindowManager() as manager:
    win = ptg.Window(
        ptg.Label("[210 bold]Hello world!"),
        ptg.Label(),
        ptg.InputField(prompt="Who are you?"),
        ptg.Label(),
        ptg.Button("Submit!")
    )
    manager.add(win)
    manager.run()
