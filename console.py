from commands import Commands
import pyfiglet

class Console(Commands):
    def __init__(self):
        super().__init__()
        self.banner = pyfiglet.figlet_format('VideoTools')

    def run(self):
        print(self.banner, flush=True)
        print("Type 'comds' for a list of commands")

        while True:
            menu_choice = input("\n>> ").lower()
            command_parts = menu_choice.split()
            command = command_parts[0]

            if command in self.commands:
                if len(command_parts) > 1:
                    params = {}
                    for arg in command_parts[1:]:
                        key, value = arg.split('=')
                        params[key] = value
                    self.commands[command](**params)
                else:
                    self.commands[command]()
            else:
                print("Invalid command.")

