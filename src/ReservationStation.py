# @file         ReservationStation.py
# @authors      Stephen

#private constants for readability
ID = 0
OPERATION = 1
TAG_I = 2
TAG_J = 3
VALUE_I = 4
VALUE_J = 5

class ReservationStation:
    """
    This class implements a generic reservation station
    """

    def __init__(self, size):
        """
        Constructor for the RS class

        @param size An integer representing the maximum amount of entries for
        this reservation station
        """
        self.size = size
        self.q = []

    def isFull(self):
        """
        Getter to determine if the RS can accept new entries
        """
        return len(self.q) == self.size

    def add(self, instructionID, op, Qi, Qj, Vi, Vj):
        """
        Adds a new entry to the end of the RS

        @param instructionID An integer representing the unqiue instruction ID
        @param op A string representing the instruction data tuple
        @param Qi A string representing the ROB entry tag that this
        instruction's first operand will come from
        @param Qj A string representing the ROB entry tag that this
        instruction's second operand will come from
        @param Vi A numeric value representing the value of this instruction's
        first operand
        @param Vj A numeric value representing the value of this instruction's
        second operand.

        We use the convention that unknown parameters are passed as None.
        Note that it is assumed that exactly one of Qi, Vi is None and exactly
        one of Qj, Vj is None at any given time.
        """
        self.q.append( [instructionID, op, Qi, Qj, Vi, Vj] )

    def remove(self, instructionID):
        """
        Given a valid instruction ID, removes the associated entry from the RS

        @param instructionID An integer representing the unique instruction ID
        """
        for i, entry in enumerate(self.q):
            if entry[ID] == instructionID:
                self.q.pop(i)
                return True
        return False

    def update(self, tag, value):
        """
        Given a tag and a value, updates the value operand of any entries with
        that tag and sets the tag to None

        @param tag A string represnting the ROB entry tag to search for and
        update the value for
        @param value A numeric value used to update the associated value for
        any tags found under search of the RS

        Note that we enforce the convention that exactly one of Qi, Vj will be
        None and exactly one of Qj, Vj will be None at any given time.
        """
        for entry in self.q:
            if entry[TAG_I] == tag:
                entry[TAG_I] = None
                entry[VALUE_I] = value
            if entry[TAG_J] == tag:
                entry[TAG_J] = None
                entry[VALUE_J] = value

    def dump(self):
        """
        Pretty-prints the RS contents
        """
        print("Reservation Station".ljust(50, '=').rjust(80, '='))
        print("Index\tID\tOperation\tQi\tQj\tVi\tVj")
        if len(self.q) < 1:
            print("\t[ empty ]")
        for idx, entry in enumerate(self.q):
            print(f"{idx}\t{entry[ID]}\t{entry[OPERATION]}\t\t{entry[TAG_I]}\t{entry[TAG_J]}\t{entry[VALUE_I]}\t{entry[VALUE_J]}")
        print()


# Test cases, run this script directly to execute
if __name__ == "__main__":
    myRS = ReservationStation(5)
    myRS.dump()
    i = 0
    while not myRS.isFull():
        print("Adding entry...")
        myRS.add(i, "ADDI", f"ROB{i}", None, None, 12)
        myRS.dump()
        i += 1

    print("RS is full!")
    for j in range(i):
        idx = i - 1 - j
        print(f"Updating ROB{idx}...")
        myRS.update(f"ROB{idx}", idx+100)
        myRS.dump()

    for j in range(i):
        print(f"Removing ID {j}...")
        myRS.remove(j)
        myRS.dump()

