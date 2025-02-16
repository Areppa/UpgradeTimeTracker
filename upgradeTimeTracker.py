"""
This is simple program to keep track of upgrades and when they will finish
Made by Aaro Halme
"""

import time

# Setting variables
COMMAND_LIST = ["p", "a", "m", "d", "q"]
upgrades = []


class Upgrade:
    """
    This class stores the ugprade and its information
    """

    def __init__(self, name, duration):
        """
        Initialization of upgrade

        All times are measured in seconds and in Unix time
        """

        self.__name = name
        self.__startTime = int(time.time())
        self.__duration = int(duration)
        self.__endTime = int(self.__startTime + self.__duration)

    def printName(self):
        print(f"{self.__name}")

    def getName(self):
        return self.__name

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
            print("Printing upgrades\n")
            printUpgrades()
        elif command == "a":
            addUpgrade()
        elif command == "m":
            modifyUpgrade()
        elif command == "d":
            deleteUpgrade()


def menu():
    command = "nocommand"
    while not command in COMMAND_LIST:
        print("\nSelect action that you want to perform: \n")

        print("- [P]rint upgrades")
        print("- [A]dd upgrade")
        print("- [M]odify upgrade")
        print("- [D]elete upgrade")
        print("- [Q]uit")

        command = input("\n> ")
        
        if not command in COMMAND_LIST:
            print("Incorrect action.\n")
        else:
            return command


def printUpgrades():
    """
    TODO List in time left order by default
    """
    if len(upgrades) == 0:
        print("No upgrades")
    else:
        for upgrade in upgrades:
            upgrade.printTimeLeft()


def addUpgrade():
    print("Adding upgrade timer\n")
    upgradeName = input("Upgrade name: ")

    # TODO Add better time format
    # For example: d h m
    while True:
        upgradeDuration = input("Upgrade duration: ")
        try:
            upgradeDuration = int(upgradeDuration)
            break
        except ValueError:
            print("Please type number")

    upgrades.append(Upgrade(upgradeName, upgradeDuration))


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
