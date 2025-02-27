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
UPGRADES_FILE = "upgrades.csv"
upgrades = []


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

    def printTimeLeft(self):
        time_left = self.__endTime - int(time.time())
        if time_left > 0:
            print(f"{self.__name}: {timeFormat(time_left)} left")
            return time_left
        else:
            print(f"{self.__name}: Upgrade completed")
            return 0

def main():

    print("Upgrade Time Tracker")

    # Program should load upgrades automatically when starting
    loadUpgradesFromFile(False)

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
    command = "no_command"
    while not command in COMMAND_LIST:
        print("\nSelect action that you want to perform: \n")

        # Print commands
        for COMMAND_PRINT in COMMAND_PRINTS:
            print(f"- {COMMAND_PRINT}")

        # Ask user for a command
        command = input("\n> ")

        # Check if command is valid
        if not command in COMMAND_LIST:
            print("Incorrect action.\n")
        else:
            return command


def saveUpgradesToFile():
    with open(UPGRADES_FILE, "w") as file:
        file.write("Name, Start Time, Duration\n")
        for upgrade in upgrades:
            file.write(f"{upgrade.getName()}, {upgrade.getStartTime()}, {upgrade.getDuration()}\n")
    print(f"Upgrades saved to {UPGRADES_FILE}")


def loadUpgradesFromFile(verbose):
    added_upgrades_counter = 0
    duplicate_upgrades_counter = 0

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

    if verbose:
        print(f"Added {added_upgrades_counter} upgrades.")
        if duplicate_upgrades_counter > 0:
            print(f"Skipped {duplicate_upgrades_counter} duplicates.")


def printUpgrades():
    print("Printing upgrades\n")
    """
    TODO List in time left order by default
    """
    if len(upgrades) == 0:
        print("No upgrades")
    else:
        for upgrade in upgrades:
            upgrade.printTimeLeft()


def addUpgrade(upgrade_start_time):
    print("Adding upgrade timer\n")
    upgrade_name = input("Upgrade name: ")

    # If upgradeStartTime is not specified -> use current time
    if upgrade_start_time == 0:
        upgrade_start_time = int(time.time())

    # TODO Add better time format
    # For example: d h m
    while True:
        upgrade_duration = input("Upgrade duration: ")
        try:
            upgrade_duration = int(upgrade_duration)
            break
        except ValueError:
            print("Please type number")

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


def timeFormat(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    formattedTime = f"{days}Days {hours}h {minutes}m {seconds}s"

    return formattedTime


if __name__ == "__main__":
    main()
