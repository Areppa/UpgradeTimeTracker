"""
This is simple program to keep track of upgrades and when they will finish
Made by Aaro Halme
"""

import time

# Setting variables
COMMAND_LIST = ["p", "a", "m", "d", "q"]
COMMAND_PRINTS = [
    "[P]rint upgrades",
    "[A]dd upgrade",
    "[M]odify upgrade",
    "[D]elete upgrade",
    "[Q]uit"
]

UPGRADES_FILE = "upgrades.csv" # File where upgrades are saved
upgrades = [] # List of upgrades


class Upgrade:
    """
    This class stores the upgrade and its information
    """

    def __init__(self, start_time, name, duration):
        """
        Initialization of upgrade

        All times are measured in seconds and in Unix time
        """

        self.__name = name
        self.__startTime = start_time
        self.__duration = int(duration)
        self.__endTime = int(self.__startTime + self.__duration)

    def getName(self):
        return self.__name

    def getStartTime(self):
        return self.__startTime

    def getDuration(self):
        return self.__duration

    def getTimeLeft(self):
        return self.__endTime - int(time.time())


def main():

    print("Upgrade Time Tracker")

    # Program should load upgrades automatically when starting
    loadUpgradesFromFile()

    while True:
        command = menu()

        if command == "q":
            print("Quiting!")
            break
        elif command == "p":
            printUpgrades()
        elif command == "a":
            addUpgrade(0)
        elif command == "m":
            modifyUpgrade()
        elif command == "d":
            deleteUpgrade()


def menu():
    """
    Basic menu system that handles user input

    :return:
    """
    command = "no_command"
    while not command in COMMAND_LIST:
        print("\nSelect action:")

        # Print commands
        for COMMAND_PRINT in COMMAND_PRINTS:
            print(f"- {COMMAND_PRINT}")

        # Ask user for a command
        command = input("\n> ").lower()

        # Check if command is valid
        if not command in COMMAND_LIST:
            print("Incorrect action.\n")
        else:
            return command


def saveUpgradesToFile():
    """
    Saves upgrades into UPGRADES_FILE

    :return:
    """
    with open(UPGRADES_FILE, "w") as file:
        file.write("Name, Start Time, Duration\n")
        for upgrade in upgrades:
            file.write(f"{upgrade.getName()}, {upgrade.getStartTime()}, {upgrade.getDuration()}\n")
    print(f"Upgrades have been successfully saved to {UPGRADES_FILE}")


def loadUpgradesFromFile():
    """
    Loads upgrades from UPGRADES_FILE and adds those into upgrades list

    :return:
    """
    added_upgrades_counter = 0
    duplicate_upgrades_counter = 0

    try:
        with open(UPGRADES_FILE, "r") as file:
            lines = file.readlines()

            # Skip the first line (descriptions)
            for line in lines[1:]:
                parts = line.strip().split(',')

                name = parts[0]
                start_time = int(parts[1])
                duration = int(parts[2])

                if any(obj.getName() == name for obj in upgrades):
                    duplicate_upgrades_counter += 1
                else:
                    upgrades.append(Upgrade(start_time, name, duration))
                    added_upgrades_counter += 1
    except FileNotFoundError:
        print(f"Could not locate {UPGRADES_FILE}. Creating a new file.")
        saveUpgradesToFile()


def printUpgrades():
    """
    Prints upgrades to user ordered by time_left

    :return:
    """
    print("Printing upgrades\n")
    """
    TODO List in time left order by default
    """
    if len(upgrades) == 0:
        print("No upgrades")
    else:
        # Sort upgrades based on time_left
        sorted_upgrades = sorted(upgrades, key=lambda x: x.getTimeLeft())
        longest_name = updateLongestVar()
        for upgrade in sorted_upgrades:
            if upgrade.getTimeLeft() > 0:
                time_left = secondsToFormattedTime(upgrade.getTimeLeft())
            else:
                time_left = "Upgrade completed"
                continue # Skips all completed upgrades

            print(f"{upgrade.getName()}: "
                  f"{(longest_name - len(upgrade.getName())) * " "} " # Have a space between name and time
                  f"{time_left}")


def addUpgrade(upgrade_start_time):
    """
    Adds upgrade to upgrades list

    :param upgrade_start_time:
    :return:
    """
    print("Adding upgrade timer\n")
    upgrade_name = input("Upgrade name: ")

    # TODO Add better time format
    # For example: d h m
    while True:
        upgrade_duration = formattedTimeToSeconds()
        try:
            upgrade_duration = int(upgrade_duration)
            break
        except ValueError:
            print("Please type number")

    # If upgradeStartTime is not specified -> use current time
    if upgrade_start_time == 0:
        upgrade_start_time = int(time.time())

    upgrades.append(Upgrade(upgrade_start_time, upgrade_name, upgrade_duration))
    saveUpgradesToFile()

def modifyUpgrade():
    print("MODIFY PLACEHOLDER")

    """
    MODIFY UPGRADE CODE HERE
    """


def deleteUpgrade():
    print("Upgrades:")

    for upgrade in upgrades:
        print(f"- {upgrade.getName()}")

    selected_upgrade = input("Which project you would like to delete?: ")

    """
    DELETE UPGRADE CODE HERE
    """


def updateLongestVar():
    """
    Checks all upgrade names and returns the longest length

    :return: int, len of the longest update name
    """
    longest_name = 0
    for upgrade in upgrades:
        if len(upgrade.getName()) > longest_name:
            longest_name = len(upgrade.getName())

    return longest_name


def secondsToFormattedTime(seconds):
    """
    Converts seconds into formatted time

    :param seconds:
    :return:
    """
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    formattedTime = ""
    if days > 0:
        formattedTime += f"{days} Days "
    if hours > 0:
        formattedTime += f"{hours}h "
    if minutes > 0:
        formattedTime += f"{minutes}m "
    if seconds > 0:
        formattedTime += f"{seconds}s"

    return formattedTime


def formattedTimeToSeconds():
    """
    Ask user for time in DD HH MM format and return that converted to seconds

    :return:
    """
    timeInput = input("Upgrade duration in DD HH MM format: ")

    days = int(timeInput.split(" ")[0])
    hours = int(timeInput.split(" ")[1])
    minutes = int(timeInput.split(" ")[2])

    # unixTime = time in seconds
    unixTime = days * 86400 + hours * 3600 + minutes * 60

    return unixTime


if __name__ == "__main__":
    main()
