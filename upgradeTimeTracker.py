"""
This is simple program to keep track of upgrades and when they will finish
Made by Aaro Halme
"""

import time

# Setting variables
COMMAND_LIST = ["p", "a", "m", "d", "q", "w", "r"]
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

    def printTimeLeft(self):
        timeLeft = self.__endTime - int(time.time())
        if timeLeft > 0:
            print(f"{self.__name}: {timeLeft}s left")
            return timeLeft
        else:
            print(f"{self.__name}: Upgrade completed")
            return 0

    def printTime(self):
        print(f"StartTime: {self.__startTime}")
        print(f"EndTime: {self.__endTime}")
        print(f"Duration: {self.__duration}")

def main():

    print("Upgrade Time Tracker")

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
        elif command == "w":
            saveUpgradesToFile()
        elif command == "r":
            loadUpgradesFromFile()


def menu():
    command = "no_command"
    while not command in COMMAND_LIST:
        print("\nSelect action that you want to perform: \n")

        print("- [P]rint upgrades")
        print("- [A]dd upgrade")
        print("- [M]odify upgrade")
        print("- [D]elete upgrade")
        print("- [W]rite to file")
        print("- [R]ead from file")
        print("- [Q]uit")

        command = input("\n> ")
        
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

def loadUpgradesFromFile():
    with open(UPGRADES_FILE, "r") as file:
        lines = file.readlines()

        # Skip the first line (descriptions)
        for line in lines[1:]:
            parts = line.strip().split(',')

            name = parts[0]
            start_time = int(parts[1])
            duration = int(parts[2])
            upgrades.append(Upgrade(start_time, name, duration))
            print(f"Added {name}")


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
        upgradeDuration = input("Upgrade duration: ")
        try:
            upgradeDuration = int(upgradeDuration)
            break
        except ValueError:
            print("Please type number")

    upgrades.append(Upgrade(upgrade_start_time, upgrade_name, upgradeDuration))


def modifyUpgrade():
    print("MODIFY PLACEHOLDER")


def deleteUpgrade():
    print("Upgrades:")

    for upgrade in upgrades:
        print(f"- {upgrade.getName()}")

    selectedUpgrade = input("Which project you would like to delete?: ")

    # THIS COULD BE BETTER OPTIMIZED!
    for upgradeIndex in len(upgrades):
        if upgrade.getName() == selectedUpgrade:
            try:
                del upgrade
                print(f"Deleted {upgrade}")
            except NameError:
                print("ERROR DELETING UPGRADE!!!")


if __name__ == "__main__":
    main()
