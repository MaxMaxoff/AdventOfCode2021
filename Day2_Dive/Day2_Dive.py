class Submarine:
    def __init__(self) -> None:
        self.aim = 0
        self.depth = 0
        self.horizontal = 0
        self.movement = {
            'forward': self.forward,
            'down': self.down,
            'up': self.up
        }

    def forward(self, move):
        self.depth += move * self.aim
        self.horizontal += move

    def down(self, move):
        self.aim += move

    def up(self, move):
        self.aim -= move


def main():
    submarine = Submarine()
    with open("Day2_Dive/Day2_Dive.txt") as f:
        for line in f:
            action, value = line.split()
            value = int(value)
            submarine.movement[action](value)
    print(submarine.depth, submarine.horizontal, submarine.depth * submarine.horizontal)

if __name__ == "__main__":
    main()