import src.obd.commands as commands


class GetAvailableCommands:
    """
    This class returns the "__mode_1__" OBD-II query commands available for a connected car
    """

    def __init__(self, connection=None):
        self.connection = connection

    def run(self):

        assert self.connection is not None, "OBD not connected"

        commands_list = commands.__dict__["modes"][1]  # mode 1
        responses_list = []
        for cmd in commands_list:
            response = self.connection.query(commands[cmd.name]).value
            responses_list.append(response)

        available_commands = [
            commands_list[i].name
            for i in range(len(commands_list))
            if responses_list[i] != None
        ]
        return available_commands
